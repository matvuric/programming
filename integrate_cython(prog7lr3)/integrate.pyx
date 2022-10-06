import cython
from cython.parallel import prange, parallel
from libc.math cimport sin
from libc.stdlib cimport malloc, free
from joblib import Parallel, delayed

ctypedef double(*f_type)(double) nogil

def integrate(f, double a, double b, int n_iter):
    cdef:
        double h = (b - a) / n_iter
        double x = a
        double sum = 0

    while x <= (b - h):
        sum += f(x)
        x += h

    cdef double res = h * ((f(a) + f(b)) / 2 + sum + h)
    return res

cdef double c_integrate(f_type f, double a, double b, int n_iter) nogil:
    cdef:
        double h = (b - a) / n_iter
        double x = a
        double sum = 0

    while x <= (b - h):
        sum += f(x)
        x += h

    cdef double res = h * ((f(a) + f(b)) / 2 + sum + h)
    return res

cdef double integrate_async(f_type f, double a, double b, int n_iter, int n_jobs):
    cdef:
        double step = (b - a) / n_jobs
        double sum = 0

        int i
        double * res = <double *> malloc(sizeof(double) * n_jobs)

    with nogil, parallel(num_threads=n_jobs):
        for i in prange(n_jobs, schedule='static'):
            res[i] = c_integrate(f, a + i * step, a + (i + 1) * step, n_iter / n_jobs)

    for i in range(n_jobs):
        sum += res[i]

    free(res)
    return sum

def integrate_joblib(f, double a, double b, int n_jobs=2, int n_iter=1000, backend=None):
    cdef double step = (b - a) / n_jobs
    with Parallel(n_jobs=n_jobs, backend=backend) as p:
        fs = (delayed(integrate)(f, a + i * step, a + (i + 1) * step, n_iter=n_iter // n_jobs) for i in range(n_jobs))
        return sum(p(fs))

cpdef integ():
    return c_integrate(sin, 0.4, 1.2, n_iter=100)

cpdef async_int():
    return integrate_async(sin, 0.4, 1.2, n_iter=100, n_jobs=6)

# python3 -m timeit -n 100 -u 'msec' -s 'from test import integrate_joblib; from math import sin' "integrate_joblib(sin, 0.4, 1.2, n_iter = 100, backend='threading')"
# python3 -m timeit -n 100000 -u 'usec' -s 'from test import async_int' "async_int()"
# python3 -m timeit -n 100000 -u 'usec' -s 'from test import integ' "integ()"

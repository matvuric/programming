from cython.parallel import prange, parallel
from libc.math cimport sin

cdef double f(double y):
    return sin(y)

def integrate(double a, double b, long n_iter):
    cdef double h = (b - a) / n_iter
    cdef double x = a
    cdef double s = 0
    cdef int i

    s = f(x) - f(b)
    for i in prange(n_iter, nogil=True):
        x += h
        s += 2 * f(x)
    result = (h / 2) * s
    return result

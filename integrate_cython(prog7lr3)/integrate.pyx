cpdef double integrate(f, double a, double b, int n_iter=10**6):
    cdef double h
    cdef double x
    cdef double int_sum

    h = (b - a) / n_iter
    x = a + h
    int_sum = 0

    while x <= (b - h):
        int_sum += f(x)
        x += h

    res = h * ((f(a) + f(b)) / 2 + int_sum)
    return round(res, 8)
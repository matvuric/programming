cpdef int fib(int n):
    cdef int a = 0
    cdef int b = 1
    while b < n:
        a, b = b, a + b

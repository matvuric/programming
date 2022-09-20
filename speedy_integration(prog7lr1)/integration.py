def integrate(f, a, b, *, n_iter=1000):
    h = (b - a) / n_iter
    x = a + h
    int_sum = 0

    while x <= (b - h):
        int_sum += f(x)
        x += h

    res = h * ((f(a) + f(b)) / 2 + int_sum)
    return round(res, 8)

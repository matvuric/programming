def integrate(f, a, b, *, n_iter=10**6):
    h = (b - a) / n_iter
    x = a + h
    s = 0

    while x <= (b - h):
        s += f(x)
        x += h

    res = h * ((f(a) + f(b)) / 2 + s)
    return round(res, 8)

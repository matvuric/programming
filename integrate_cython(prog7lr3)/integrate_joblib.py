from joblib import Parallel, delayed


def integrate(f, a, b, *, n_iter=10**6):
    h = (b - a) / n_iter
    x = a + h
    s = 0

    while x <= (b - h):
        s += f(x)
        x += h

    res = h * ((f(a) + f(b)) / 2 + s)
    return round(res, 8)


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000, backend=None):
    h = (b - a) / n_jobs
    with Parallel(n_jobs=n_jobs, backend=backend) as p:
        fs = (delayed(integrate)(f, a + i * (h + 1), a + (i + 1) * h, n_iter=n_iter // n_jobs) for i in range(n_jobs))
        return sum(p(fs))

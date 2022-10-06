import concurrent.futures as ftres
from functools import partial


def integrate(f, a, b, *, n_iter=10**6):
    h = (b - a) / n_iter
    x = a + h
    int_sum = 0

    while x <= (b - h):
        int_sum += f(x)
        x += h

    res = h * ((f(a) + f(b)) / 2 + int_sum)
    return round(res, 8)


def integrate_async(f, a, b, *, n_jobs=2, n_iter=10**6):
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return round(sum(f.result() for f in ftres.as_completed(fs)), 8)
import pytest
import math
from integrate import integrate, integrate_async


def test_sin_async2():
    assert integrate_async(math.sin, 0, 2, n_iter=1000) == integrate(math.sin, 0, 2, n_iter=1000)
    assert integrate_async(math.sin, 0, 2, n_iter=10000) == integrate(math.sin, 0, 2, n_iter=10000)
    assert integrate_async(math.sin, 0, 2, n_iter=100000) == integrate(math.sin, 0, 2, n_iter=100000)
    assert integrate_async(math.sin, 1, 20, n_iter=1000) == integrate(math.sin, 1, 20, n_iter=1000)
    assert integrate_async(math.sin, 1, 20, n_iter=10000) == integrate(math.sin, 1, 20, n_iter=10000)
    assert integrate_async(math.sin, 1, 20, n_iter=100000) == integrate(math.sin, 1, 20, n_iter=100000)


def test_cos_async2():
    assert integrate_async(math.cos, 0, 2, n_iter=1000) == integrate(math.cos, 0, 2, n_iter=1000)
    assert integrate_async(math.cos, 0, 2, n_iter=10000) == integrate(math.cos, 0, 2, n_iter=10000)
    assert integrate_async(math.cos, 0, 2, n_iter=100000) == integrate(math.cos, 0, 2, n_iter=100000)
    assert integrate_async(math.cos, 1, 20, n_iter=1000) == integrate(math.cos, 1, 20, n_iter=1000)
    assert integrate_async(math.cos, 1, 20, n_iter=10000) == integrate(math.cos, 1, 20, n_iter=10000)
    assert integrate_async(math.cos, 1, 20, n_iter=100000) == integrate(math.cos, 1, 20, n_iter=100000)


def test_sin_async4():
    assert integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=1000) == integrate(math.sin, 0, 2, n_iter=1000)
    assert integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=10000) == integrate(math.sin, 0, 2, n_iter=10000)
    assert integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=100000) == integrate(math.sin, 0, 2, n_iter=100000)
    assert integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=1000) == integrate(math.sin, 1, 20, n_iter=1000)
    assert integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=10000) == integrate(math.sin, 1, 20, n_iter=10000)
    assert integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=100000) == integrate(math.sin, 1, 20, n_iter=100000)


def test_cos_async4():
    assert integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=1000) == integrate(math.cos, 0, 2, n_iter=1000)
    assert integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=10000) == integrate(math.cos, 0, 2, n_iter=10000)
    assert integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=100000) == integrate(math.cos, 0, 2, n_iter=100000)
    assert integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=1000) == integrate(math.cos, 1, 20, n_iter=1000)
    assert integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=10000) == integrate(math.cos, 1, 20, n_iter=10000)
    assert integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=100000) == integrate(math.cos, 1, 20, n_iter=100000)

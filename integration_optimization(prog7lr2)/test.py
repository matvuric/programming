import unittest
import math
from integrate import integrate, integrate_async


class TestIntegrate(unittest.TestCase):
    def test_sin_async2(self):
        self.assertEqual(integrate_async(math.sin, 0, 2, n_iter=1000), integrate(math.sin, 0, 2, n_iter=1000))
        self.assertEqual(integrate_async(math.sin, 0, 2, n_iter=10000), integrate(math.sin, 0, 2, n_iter=10000))
        self.assertEqual(integrate_async(math.sin, 0, 2, n_iter=100000), integrate(math.sin, 0, 2, n_iter=100000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_iter=1000), integrate(math.sin, 1, 20, n_iter=1000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_iter=10000), integrate(math.sin, 1, 20, n_iter=10000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_iter=100000), integrate(math.sin, 1, 20, n_iter=100000))

    def test_cos_async2(self):
        self.assertEqual(integrate_async(math.cos, 0, 2, n_iter=1000), integrate(math.cos, 0, 2, n_iter=1000))
        self.assertEqual(integrate_async(math.cos, 0, 2, n_iter=10000), integrate(math.cos, 0, 2, n_iter=10000))
        self.assertEqual(integrate_async(math.cos, 0, 2, n_iter=100000), integrate(math.cos, 0, 2, n_iter=100000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_iter=1000), integrate(math.cos, 1, 20, n_iter=1000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_iter=10000), integrate(math.cos, 1, 20, n_iter=10000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_iter=100000), integrate(math.cos, 1, 20, n_iter=100000))

    def test_sin_async4(self):
        self.assertEqual(integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=1000),
                         integrate(math.sin, 0, 2, n_iter=1000))
        self.assertEqual(integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=10000),
                         integrate(math.sin, 0, 2, n_iter=10000))
        self.assertEqual(integrate_async(math.sin, 0, 2, n_jobs=4, n_iter=100000),
                         integrate(math.sin, 0, 2, n_iter=100000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=1000),
                         integrate(math.sin, 1, 20, n_iter=1000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=10000),
                         integrate(math.sin, 1, 20, n_iter=10000))
        self.assertEqual(integrate_async(math.sin, 1, 20, n_jobs=4, n_iter=100000),
                         integrate(math.sin, 1, 20, n_iter=100000))

    def test_cos_async4(self):
        self.assertEqual(integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=1000),
                         integrate(math.cos, 0, 2, n_iter=1000))
        self.assertEqual(integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=10000),
                         integrate(math.cos, 0, 2, n_iter=10000))
        self.assertEqual(integrate_async(math.cos, 0, 2, n_jobs=4, n_iter=100000),
                         integrate(math.cos, 0, 2, n_iter=100000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=1000),
                         integrate(math.cos, 1, 20, n_iter=1000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=10000),
                         integrate(math.cos, 1, 20, n_iter=10000))
        self.assertEqual(integrate_async(math.cos, 1, 20, n_jobs=4, n_iter=100000),
                         integrate(math.cos, 1, 20, n_iter=100000))


if __name__ == '__main__':
    unittest.main(verbosity=1)

import unittest
from main import CurrenciesList


class CurrencyInfoTest(unittest.TestCase):
    def test_object_type(self):
        self.assertIsInstance(CurrenciesList(), type(CurrenciesList()))

    def test_instances_ids(self):
        x = CurrenciesList()
        y = CurrenciesList()
        self.assertEqual(id(x), id(y))

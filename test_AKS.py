import unittest

from AKS import Property, aks_primality


class Test(unittest.TestCase):
    def test_7_is_prime(self):
        self.assertEqual(Property.PRIME, aks_primality(7))

    def test_41_43_are_prime(self):
        self.assertEqual(Property.PRIME, aks_primality(41))
        self.assertEqual(Property.PRIME, aks_primality(43))

    def test_7919_is_prime(self):
        self.assertEqual(Property.PRIME, aks_primality(7919))

    def test_6_is_composite(self):
        self.assertEqual(Property.COMPOSITE, aks_primality(6))

    def test_9_12_are_composite(self):
        self.assertEqual(Property.COMPOSITE, aks_primality(9))
        self.assertEqual(Property.COMPOSITE, aks_primality(12))


if __name__ == '__main__':
    unittest.main()
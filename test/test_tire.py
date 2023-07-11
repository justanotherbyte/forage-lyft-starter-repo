import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestTires(unittest.TestCase):
    def test_carrigan(self):
        values1 = (0.1, 0.5, 0.6, 0.93)
        values2 = (0.1, 0.2, 0.3, 0.4)
        
        tire1 = CarriganTire(values1)
        tire2 = CarriganTire(values2)

        self.assertTrue(tire1.needs_service())
        self.assertFalse(tire2.needs_service())

    def test_octoprime(self):
        values1 = (1.0, 0.9, 0.9, 0.9)
        values2 = (0.1, 0.2, 0.3, 0.4)
        
        tire1 = CarriganTire(values1)
        tire2 = CarriganTire(values2)

        self.assertTrue(tire1.needs_service())
        self.assertFalse(tire2.needs_service())

if __name__ == "__main__":
    unittest.main()
import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngines(unittest.TestCase):
    def test_capulet(self):
        engine1 = CapuletEngine(10_000, 40_000)
        engine2 = CapuletEngine(10_000, 20_000)
        self.assertTrue(engine1.needs_service())
        self.assertFalse(engine2.needs_service())

    def test_sternman(self):
        engine1 = SternmanEngine(True)
        engine2 = SternmanEngine(False)
        self.assertTrue(engine1.needs_service())
        self.assertFalse(engine2.needs_service())

    def test_willoughby(self):
        engine1 = WilloughbyEngine(10_000, 70_000)
        engine2 = WilloughbyEngine(10_000, 20_000)
        self.assertTrue(engine1.needs_service())
        self.assertFalse(engine2.needs_service())

if __name__ == "__main__":
    unittest.main()
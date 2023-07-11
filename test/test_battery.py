import unittest
from datetime import datetime, timedelta

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestBatteries(unittest.TestCase):
    def test_spindler(self):
        today = datetime.today()
        three_years_ago = (today - timedelta(days=365 * 3))
        one_year_ago = (today - timedelta(days=365))

        battery1 = SpindlerBattery(three_years_ago, today)
        battery2 = SpindlerBattery(one_year_ago, today)

        self.assertTrue(battery1.needs_service())
        self.assertFalse(battery2.needs_service())

    def test_nubbin(self):
        today = datetime.today()
        four_years_ago = (today - timedelta(days=365 * 4))
        one_year_ago = (today - timedelta(days=365))

        battery1 = SpindlerBattery(four_years_ago, today)
        battery2 = SpindlerBattery(one_year_ago, today)

        self.assertTrue(battery1.needs_service())
        self.assertFalse(battery2.needs_service())

if __name__ == "__main__":
    unittest.main()
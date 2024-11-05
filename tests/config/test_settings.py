# tests/config/test_settings.py

import unittest
from config.settings import COST_THRESHOLD

class TestSettings(unittest.TestCase):

    def test_cost_threshold(self):
        self.assertIsInstance(COST_THRESHOLD, (int, float))
        self.assertGreater(COST_THRESHOLD, 0, "COST_THRESHOLD should be greater than zero")

if __name__ == '__main__':
    unittest.main()

# tests/core/test_data_processing.py

import unittest
from core.data_processing import aggregate_costs, filter_high_costs

class TestDataProcessing(unittest.TestCase):

    def test_aggregate_costs(self):
        data = [
            {"service": "EC2", "cost": 100},
            {"service": "S3", "cost": 50},
            {"service": "EC2", "cost": 150},
        ]
        result = aggregate_costs(data)
        expected_result = {"EC2": 250, "S3": 50}
        self.assertEqual(result, expected_result)

    def test_filter_high_costs(self):
        data = {"EC2": 250, "S3": 50}
        threshold = 100
        result = filter_high_costs(data, threshold)
        expected_result = {"EC2": 250}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

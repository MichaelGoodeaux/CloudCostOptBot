# tests/providers/test_gcp_provider.py

import unittest
from unittest.mock import patch
from providers.gcp import gcp_data_collector

class TestGCPDataCollector(unittest.TestCase):

    @patch('providers.gcp.googleapiclient.discovery.build')
    def test_collect_cost_data(self, mock_build):
        mock_service = mock_build.return_value
        mock_service.projects().reports().query().execute.return_value = {
            "Cost": "300.0"
        }
        
        result = gcp_data_collector.collect_cost_data()
        expected_result = {"Cost": "300.0"}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

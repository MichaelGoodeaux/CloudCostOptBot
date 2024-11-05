# tests/providers/test_azure_provider.py

import unittest
from unittest.mock import patch
from providers.azure import azure_data_collector

class TestAzureDataCollector(unittest.TestCase):

    @patch('providers.azure.AzureCostManagementClient')
    def test_collect_cost_data(self, mock_client):
        mock_client_instance = mock_client.return_value
        mock_client_instance.query.usage.return_value = {"Total": {"Cost": "200.0"}}
        
        result = azure_data_collector.collect_cost_data()
        expected_result = {"Total": {"Cost": "200.0"}}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

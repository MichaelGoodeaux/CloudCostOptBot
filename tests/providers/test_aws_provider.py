# tests/providers/test_aws_provider.py

import unittest
from unittest.mock import patch
from providers.aws import aws_data_collector

class TestAWSDataCollector(unittest.TestCase):

    @patch('providers.aws.boto3.client')
    def test_collect_cost_data(self, mock_boto_client):
        mock_client = mock_boto_client.return_value
        mock_client.get_cost_and_usage.return_value = {
            "ResultsByTime": [
                {"Total": {"UnblendedCost": {"Amount": "100.0"}}}
            ]
        }
        result = aws_data_collector.collect_cost_data()
        expected_result = [{"Total": {"UnblendedCost": {"Amount": "100.0"}}}]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

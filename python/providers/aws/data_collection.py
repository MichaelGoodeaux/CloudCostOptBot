# aws/data_collection.py - Collects cost data from AWS

import boto3
from botocore.exceptions import BotoCoreError, ClientError

def collect_cost_data():
    """
    Collects cost data from AWS Cost Explorer.
    Returns:
        list: List of cost data entries with categories and cost values.
    """
    try:
        # Initialize the AWS Cost Explorer client
        client = boto3.client("ce")

        # Define the time range for cost data (e.g., last 30 days)
        time_period = {
            "Start": "2023-01-01",  # Example start date
            "End": "2023-01-31"     # Example end date
        }

        # Call Cost Explorer API
        response = client.get_cost_and_usage(
            TimePeriod=time_period,
            Granularity="DAILY",
            Metrics=["UnblendedCost"]
        )

        # Extract and return cost data
        cost_data = response.get("ResultsByTime", [])
        return cost_data

    except (BotoCoreError, ClientError) as error:
        print(f"Error collecting AWS cost data: {error}")
        return []

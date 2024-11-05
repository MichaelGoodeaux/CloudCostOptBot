# azure/data_collection.py - Collects cost data from Azure

from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from datetime import datetime, timedelta

def collect_cost_data():
    """
    Collects cost data from Azure Cost Management API.
    Returns:
        list: List of cost data entries with categories and cost values.
    """
    try:
        # Initialize the Azure Cost Management client
        credential = DefaultAzureCredential()
        client = CostManagementClient(credential)

        # Define time range (e.g., last 30 days)
        time_period = {
            "start": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
            "end": datetime.now().strftime("%Y-%m-%d"),
        }

        # Retrieve cost data
        response = client.query.usage(
            scope="/subscriptions/YOUR_SUBSCRIPTION_ID",  # Replace with your subscription ID
            parameters={
                "type": "ActualCost",
                "timeframe": "Custom",
                "timePeriod": time_period,
            }
        )

        # Extract and return cost data
        cost_data = response.value
        return cost_data

    except Exception as error:
        print(f"Error collecting Azure cost data: {error}")
        return []

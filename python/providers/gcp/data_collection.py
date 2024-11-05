# gcp/data_collection.py - Collects cost data from GCP

from google.cloud import billing_v1

def collect_cost_data():
    """
    Collects cost data from Google Cloud Billing API.
    Returns:
        list: List of cost data entries with categories and cost values.
    """
    try:
        # Initialize the Billing client
        client = billing_v1.CloudBillingClient()
        project_id = "projects/YOUR_PROJECT_ID"  # Replace with your GCP project ID

        # Query billing data
        response = client.get_project_billing_info(name=project_id)

        # Process and return cost data
        cost_data = response
        return cost_data

    except Exception as error:
        print(f"Error collecting GCP cost data: {error}")
        return []

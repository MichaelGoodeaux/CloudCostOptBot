# index.py - Main Lambda function for cost optimization in ./infrastructure/aws/lambda

from python.core.data_processing import aggregate_costs, filter_high_costs
from python.providers.aws import aws_data_collector
from python.providers.azure import azure_data_collector
from python.providers.gcp import gcp_data_collector
from python.config.settings import COST_THRESHOLD, REPORT_FREQUENCY
import json

def handler(event, context):
    # Collect data from AWS, Azure, and GCP
    aws_cost_data = aws_data_collector.collect_cost_data()
    azure_cost_data = azure_data_collector.collect_cost_data()
    gcp_cost_data = gcp_data_collector.collect_cost_data()

    # Combine and process the data
    all_cost_data = aws_cost_data + azure_cost_data + gcp_cost_data
    aggregated_data = aggregate_costs(all_cost_data)
    high_cost_data = filter_high_costs(aggregated_data, threshold=COST_THRESHOLD)

    # Output results for debugging
    print("High-cost resources identified:")
    print(high_cost_data)

    # Return response for monitoring
    return {
        "statusCode": 200,
        "body": json.dumps("Cost optimization task completed successfully.")
    }

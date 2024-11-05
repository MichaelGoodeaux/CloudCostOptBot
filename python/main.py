# main.py - Multi-cloud support with flexible provider selection

from python.config.settings import ENABLE_AWS, ENABLE_AZURE, ENABLE_GCP, COST_THRESHOLD
from python.core.data_processing import aggregate_costs, filter_high_costs, format_cost_data
from python.core.recommendations import generate_recommendations, prioritize_recommendations
from python.core.notifications import send_slack_notification, format_recommendations_for_notification

# Import provider-specific modules conditionally
if ENABLE_AWS:
    from python.providers.aws.data_collection import collect_cost_data as collect_aws_cost_data
    from python.providers.aws.automation import stop_idle_instances as stop_aws_idle_instances

if ENABLE_AZURE:
    from python.providers.azure.data_collection import collect_cost_data as collect_azure_cost_data
    from python.providers.azure.automation import stop_idle_vms as stop_azure_idle_vms

if ENABLE_GCP:
    from python.providers.gcp.data_collection import collect_cost_data as collect_gcp_cost_data
    from python.providers.gcp.automation import stop_idle_instances as stop_gcp_idle_instances

def process_provider(provider_name, collect_cost_data, stop_idle_resources):
    print(f"Processing {provider_name} data...")

    # Step 1: Collect cost data
    cost_data = collect_cost_data()
    if not cost_data:
        print(f"No cost data available for {provider_name} or error fetching data.")
        return

    # Step 2: Process the data (aggregate, filter, and format)
    aggregated_data = aggregate_costs(cost_data)
    high_cost_data = filter_high_costs(aggregated_data, threshold=COST_THRESHOLD)
    formatted_cost_data = format_cost_data(high_cost_data)
    print(f"Aggregated high-cost data for {provider_name}:")
    print(formatted_cost_data)

    # Step 3: Generate and prioritize recommendations
    recommendations = generate_recommendations(high_cost_data)
    prioritized_recommendations = prioritize_recommendations(recommendations)
    formatted_recommendations = format_recommendations_for_notification(prioritized_recommendations)

    # Step 4: Send recommendations as a notification
    print(f"Sending recommendations for {provider_name} to Slack...")
    send_slack_notification(formatted_recommendations)

    # Step 5: (Optional) Take automation actions
    idle_resources = stop_idle_resources()
    if idle_resources:
        print(f"{provider_name} automated action taken: Stopped resources: {idle_resources}")
    else:
        print(f"No idle resources found or error stopping resources in {provider_name}.")

def main():
    # Run the process for each enabled provider
    if ENABLE_AWS:
        process_provider("AWS", collect_aws_cost_data, stop_aws_idle_instances)
    if ENABLE_AZURE:
        process_provider("Azure", collect_azure_cost_data, stop_azure_idle_vms)
    if ENABLE_GCP:
        process_provider("GCP", collect_gcp_cost_data, stop_gcp_idle_instances)

if __name__ == "__main__":
    main()

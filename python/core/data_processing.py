# data_processing.py - Contains functions for processing raw cost data

def aggregate_costs(data):
    """
    Aggregates raw cost data by category (e.g., service, resource type).
    Args:
        data (list): List of raw cost data dictionaries.

    Returns:
        dict: Aggregated cost data by category.
    """
    aggregated_data = {}
    for entry in data:
        category = entry.get("category", "unknown")
        cost = entry.get("cost", 0)
        if category not in aggregated_data:
            aggregated_data[category] = 0
        aggregated_data[category] += cost
    return aggregated_data


def filter_high_costs(data, threshold):
    """
    Filters out entries that exceed a certain cost threshold.
    Args:
        data (dict): Aggregated cost data.
        threshold (float): Cost threshold for filtering.

    Returns:
        dict: Filtered data with only entries above the threshold.
    """
    high_cost_items = {k: v for k, v in data.items() if v > threshold}
    return high_cost_items


def format_cost_data(data):
    """
    Formats cost data for readability in reports or notifications.
    Args:
        data (dict): Aggregated or filtered cost data.

    Returns:
        str: Formatted string representation of cost data.
    """
    formatted_data = "\n".join([f"{category}: ${cost:.2f}" for category, cost in data.items()])
    return formatted_data

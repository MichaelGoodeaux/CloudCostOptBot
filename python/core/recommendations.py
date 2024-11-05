# recommendations.py - Generates recommendations for cost optimization

def generate_recommendations(data):
    """
    Generates recommendations based on high-cost categories.
    Args:
        data (dict): Aggregated and filtered cost data.

    Returns:
        list: List of recommendation strings.
    """
    recommendations = []
    for category, cost in data.items():
        # Example recommendation based on cost category
        recommendations.append(f"Consider rightsizing or removing unused resources in {category} to reduce costs.")
    return recommendations


def prioritize_recommendations(recommendations):
    """
    Prioritizes recommendations based on impact (e.g., potential savings).
    Args:
        recommendations (list): List of recommendation strings.

    Returns:
        list: Prioritized recommendations.
    """
    # Dummy prioritization logic - could be enhanced based on actual cost impact
    prioritized = sorted(recommendations, key=lambda x: x.count("reduce"), reverse=True)
    return prioritized

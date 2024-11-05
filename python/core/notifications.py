# notifications.py - Sends notifications to the specified communication platform

import os
import requests

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_notification(message):
    """
    Sends a notification message to a Slack channel using a webhook.
    Args:
        message (str): The message to send.

    Returns:
        response: Response object from the Slack API request.
    """
    if not SLACK_WEBHOOK_URL:
        print("Error: SLACK_WEBHOOK_URL is not configured.")
        return None

    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
    return response


def format_recommendations_for_notification(recommendations):
    """
    Formats recommendations as a message for notifications.
    Args:
        recommendations (list): List of recommendation strings.

    Returns:
        str: Formatted message for notifications.
    """
    formatted_message = "Cost Optimization Recommendations:\n" + "\n".join(recommendations)
    return formatted_message

# settings.py - General configuration settings for the cost optimization bot

import os

# Enable or disable each provider based on environment variables
ENABLE_AWS = os.getenv("ENABLE_AWS", "false").lower() == "true"
ENABLE_AZURE = os.getenv("ENABLE_AZURE", "false").lower() == "true"
ENABLE_GCP = os.getenv("ENABLE_GCP", "false").lower() == "true"

# Other settings
COST_THRESHOLD = float(os.getenv("COST_THRESHOLD", 100.0))
REPORT_FREQUENCY = os.getenv("REPORT_FREQUENCY", "daily")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

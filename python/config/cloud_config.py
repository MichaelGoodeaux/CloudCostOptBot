# cloud_config.py - Cloud provider-specific configurations

import os

# AWS Configuration
AWS_CONFIG = {
    "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
    "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "region": os.getenv("AWS_REGION", "us-east-1"),
}

# Azure Configuration
AZURE_CONFIG = {
    "client_id": os.getenv("AZURE_CLIENT_ID"),
    "client_secret": os.getenv("AZURE_CLIENT_SECRET"),
    "tenant_id": os.getenv("AZURE_TENANT_ID"),
    "subscription_id": os.getenv("AZURE_SUBSCRIPTION_ID"),
    "region": os.getenv("AZURE_REGION", "eastus"),
}

# GCP Configuration
GCP_CONFIG = {
    "service_account_key": os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
    "project_id": os.getenv("GCP_PROJECT_ID"),
    "region": os.getenv("GCP_REGION", "us-central1"),
}

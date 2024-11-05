#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install AWS CLI
install_aws_cli() {
    echo "AWS CLI not found. Installing AWS CLI..."
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    rm -rf awscliv2.zip aws
    echo "AWS CLI installed successfully."
}

# Function to install Azure CLI
install_azure_cli() {
    echo "Azure CLI not found. Installing Azure CLI..."
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    echo "Azure CLI installed successfully."
}

# Function to install Google Cloud SDK
install_gcloud_cli() {
    echo "Google Cloud SDK not found. Installing Google Cloud SDK..."
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    sudo apt-get install -y apt-transport-https ca-certificates gnupg
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    sudo apt-get update && sudo apt-get install -y google-cloud-sdk
    echo "Google Cloud SDK installed successfully."
}

# Step 1: Install CLI tools if missing
echo "Checking for required CLI tools..."

if ! command_exists aws; then
    install_aws_cli
fi

if ! command_exists az; then
    install_azure_cli
fi

if ! command_exists gcloud; then
    install_gcloud_cli
fi

echo "All required CLI tools are installed."

# Step 2: Set environment variables and check provider usage
echo "Setting environment variables..."

# AWS
export AWS_REGION="${AWS_REGION:-us-east-1}"
export AWS_ACCOUNT_ID="${AWS_ACCOUNT_ID}"
export AWS_BUCKET_NAME="${AWS_BUCKET_NAME:-cost-opt-bucket}"

# Azure
export AZURE_REGION="${AZURE_REGION:-eastus}"
export AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-cost-opt-rg}"
export AZURE_STORAGE_ACCOUNT_NAME="${AZURE_STORAGE_ACCOUNT_NAME:-costoptstorage}"
export AZURE_FUNCTION_APP_NAME="${AZURE_FUNCTION_APP_NAME:-costOptimizationFunction}"

# GCP
export GCP_BUCKET_NAME="${GCP_BUCKET_NAME:-cost-opt-bucket}"
export GCP_REGION="${GCP_REGION:-us-central1}"
export GCP_FUNCTION_NAME="${GCP_FUNCTION_NAME:-costOptimizationFunction}"

# Step 3: Check if each provider's necessary environment variables are set
USE_AWS=${AWS_ACCOUNT_ID:+true}
USE_AZURE=${AZURE_RESOURCE_GROUP:+true}
USE_GCP=${GCP_BUCKET_NAME:+true}

if [ -z "$USE_AWS" ] && [ -z "$USE_AZURE" ] && [ -z "$USE_GCP" ]; then
  echo "No provider environment variables are set. Please set at least one provider's variables and try again."
  exit 1
fi

# Step 4: Deploy resources for each cloud provider if enabled

# AWS Setup and Deployment
if [ "$USE_AWS" ]; then
  echo "Setting up AWS resources..."
  echo "Creating AWS S3 bucket for Lambda code storage..."
  aws s3 mb s3://$AWS_BUCKET_NAME --region $AWS_REGION || true  # Ignore if bucket already exists

  echo "Deploying AWS Lambda function..."
  ./infrastructure/aws/deploy_aws.sh  # Ensure this script is configured to use $AWS_BUCKET_NAME
fi

# Azure Setup and Deployment
if [ "$USE_AZURE" ]; then
  echo "Setting up Azure resources..."
  echo "Creating Azure Storage Account and Resource Group..."
  az group create --name $AZURE_RESOURCE_GROUP --location $AZURE_REGION || true  # Ignore if exists
  az storage account create --name $AZURE_STORAGE_ACCOUNT_NAME --resource-group $AZURE_RESOURCE_GROUP --location $AZURE_REGION --sku Standard_LRS || true

  echo "Deploying Azure Function..."
  ./infrastructure/azure/deploy_azure.sh  # Ensure this script uses the repository variables set above
fi

# GCP Setup and Deployment
if [ "$USE_GCP" ]; then
  echo "Setting up GCP resources..."
  echo "Creating Google Cloud Storage bucket..."
  gsutil mb -l $GCP_REGION gs://$GCP_BUCKET_NAME || true  # Ignore if bucket already exists

  echo "Deploying GCP Function..."
  ./infrastructure/gcp/deploy_gcp.sh  # Ensure this script uses the repository variables set above
fi

echo "Bootstrap completed successfully for the specified cloud providers!"

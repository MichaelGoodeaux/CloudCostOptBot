#!/bin/bash

# Check for required environment variables
if [[ -z "$GCP_BUCKET_NAME" || -z "$GCP_REGION" || -z "$GCP_FUNCTION_NAME" ]]; then
  echo "Error: GCP_BUCKET_NAME, GCP_REGION, and GCP_FUNCTION_NAME environment variables must be set."
  exit 1
fi

# Define paths
FUNCTION_CODE_PATH="./infrastructure/gcp/function"  # Path to GCP function code
PYTHON_CODE_PATH="./python"                         # Path to shared Python code
ZIP_FILE="function_package.zip"                     # Output zip file name

# Remove old zip file if it exists
rm -f $ZIP_FILE

# Create a zip file with both function code and python directory
zip -r $ZIP_FILE $FUNCTION_CODE_PATH $PYTHON_CODE_PATH

# Upload zip file to Google Cloud Storage
gsutil cp $ZIP_FILE gs://$GCP_BUCKET_NAME/$ZIP_FILE

# Deploy the function using Google Cloud Functions
gcloud functions deploy $GCP_FUNCTION_NAME \
  --runtime python39 \
  --trigger-http \
  --source gs://$GCP_BUCKET_NAME/$ZIP_FILE \
  --entry-point handler \
  --region $GCP_REGION

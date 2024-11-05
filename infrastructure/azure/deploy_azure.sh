#!/bin/bash

# Check for required environment variables
if [[ -z "$AZURE_STORAGE_ACCOUNT_NAME" || -z "$AZURE_REGION" || -z "$AZURE_FUNCTION_APP_NAME" || -z "$AZURE_RESOURCE_GROUP" ]]; then
  echo "Error: AZURE_STORAGE_ACCOUNT_NAME, AZURE_REGION, AZURE_FUNCTION_APP_NAME, and AZURE_RESOURCE_GROUP environment variables must be set."
  exit 1
fi

# Define paths
FUNCTION_CODE_PATH="./infrastructure/azure/lambda"  # Path to Azure function code
PYTHON_CODE_PATH="./python"                         # Path to shared Python code
ZIP_FILE="function_package.zip"                     # Output zip file name

# Remove old zip file if it exists
rm -f $ZIP_FILE

# Create a zip file with both function code and python directory
zip -r $ZIP_FILE $FUNCTION_CODE_PATH $PYTHON_CODE_PATH

# Upload zip file to Azure Storage
az storage blob upload --account-name $AZURE_STORAGE_ACCOUNT_NAME --container-name $AZURE_FUNCTION_APP_NAME --file $ZIP_FILE --name $ZIP_FILE

# Get the URL of the uploaded zip file
CODE_BLOB_URL=$(az storage blob url --account-name $AZURE_STORAGE_ACCOUNT_NAME --container-name $AZURE_FUNCTION_APP_NAME --name $ZIP_FILE --output tsv)

# Deploy Azure Bicep with the URL of the uploaded zip package
az deployment group create --resource-group $AZURE_RESOURCE_GROUP --template-file infrastructure/azure/main.bicep --parameters location=$AZURE_REGION functionName=$AZURE_FUNCTION_APP_NAME storageAccountName=$AZURE_STORAGE_ACCOUNT_NAME codeBlobUrl=$CODE_BLOB_URL

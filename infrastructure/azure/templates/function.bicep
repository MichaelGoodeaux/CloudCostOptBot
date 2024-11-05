// function.bicep

param location string
param functionName string
param storageAccountName string
param codeBlobUrl string  // URL of the uploaded zip package

// Storage Account for the Function App
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// Construct the blob endpoint using the environment function
var storageAccountBlobEndpoint = 'https://${storageAccount.name}.blob.${environment().suffixes.storage}'

// App Service Plan for the Function App
resource appServicePlan 'Microsoft.Web/serverfarms@2021-02-01' = {
  name: '${functionName}-plan'
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
}

// Azure Function App
resource functionApp 'Microsoft.Web/sites@2021-02-01' = {
  name: functionName
  location: location
  kind: 'functionapp'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: storageAccountBlobEndpoint  // Sets the blob endpoint using environment function
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
        {
          name: 'WEBSITE_RUN_FROM_PACKAGE'
          value: codeBlobUrl  // Uses the code package URL from the parameter
        }
      ]
    }
  }
}

// Output function name and URL for access
output functionName string = functionApp.name
output functionUrl string = 'https://${functionApp.properties.defaultHostName}/api/YourFunctionEndpoint'

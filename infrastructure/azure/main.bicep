// main.bicep - Azure Bicep file for deploying Azure Function

param location string
param functionName string
param storageAccountName string
param codeBlobUrl string  // URL of the uploaded zip package

module function './templates/function.bicep' = {
  name: '${functionName}-function'
  params: {
    location: location
    functionName: functionName
    storageAccountName: storageAccountName
    codeBlobUrl: codeBlobUrl
  }
}

module schedule './templates/schedule.bicep' = {
  name: '${functionName}-schedule'
  params: {
    functionName: function.outputs.functionName
    schedule: '0 0 * * *' // Runs daily at midnight
  }
}

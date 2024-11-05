// schedule.bicep - Timer-based trigger for Azure Function

param functionName string
param schedule string

resource functionSchedule 'Microsoft.Web/sites/functions@2021-02-01' = {
  name: '${functionName}/timerTrigger'
  properties: {
    config: {
      schedule: schedule
      bindingType: 'timerTrigger'
    }
  }
}

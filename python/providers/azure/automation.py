# azure/automation.py - Automation actions for Azure cost optimization

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def stop_idle_vms():
    """
    Stops idle Azure VMs to reduce costs.
    Returns:
        list: List of stopped VM IDs.
    """
    try:
        # Initialize the Azure Compute client
        credential = DefaultAzureCredential()
        client = ComputeManagementClient(credential, "YOUR_SUBSCRIPTION_ID")  # Replace with your subscription ID

        # List and stop idle VMs
        stopped_vms = []
        for vm in client.virtual_machines.list_all():
            if vm.instance_view.statuses[1].code == "PowerState/running":
                client.virtual_machines.begin_deallocate("resourceGroupName", vm.name)  # Replace with resource group name
                stopped_vms.append(vm.name)
                print(f"Stopped VM: {vm.name}")
        return stopped_vms

    except Exception as error:
        print(f"Error stopping Azure VMs: {error}")
        return []

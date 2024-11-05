# gcp/automation.py - Automation actions for GCP cost optimization

from google.cloud import compute_v1

def stop_idle_instances():
    """
    Stops idle GCP instances to reduce costs.
    Returns:
        list: List of stopped instance names.
    """
    try:
        # Initialize the Compute client
        client = compute_v1.InstancesClient()
        project_id = "YOUR_PROJECT_ID"  # Replace with your GCP project ID
        zone = "YOUR_INSTANCE_ZONE"     # Replace with the instance zone

        # List and stop idle instances
        stopped_instances = []
        instances = client.list(project=project_id, zone=zone)
        for instance in instances:
            if instance.status == "RUNNING":
                client.stop(project=project_id, zone=zone, instance=instance.name)
                stopped_instances.append(instance.name)
                print(f"Stopped instance: {instance.name}")
        return stopped_instances

    except Exception as error:
        print(f"Error stopping GCP instances: {error}")
        return []

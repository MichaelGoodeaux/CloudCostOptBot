# aws/automation.py - Automation actions for AWS cost optimization

import boto3
from botocore.exceptions import BotoCoreError, ClientError

def stop_idle_instances():
    """
    Stops idle EC2 instances to reduce costs.
    Returns:
        list: List of stopped instance IDs.
    """
    try:
        # Initialize the EC2 client
        client = boto3.client("ec2")
        
        # Describe EC2 instances with filter for idle state (e.g., running with no recent activity)
        response = client.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])

        # Collect instance IDs to stop
        instance_ids = [instance["InstanceId"] for reservation in response["Reservations"] for instance in reservation["Instances"]]
        
        # Stop instances if any are idle
        if instance_ids:
            client.stop_instances(InstanceIds=instance_ids)
            print(f"Stopped instances: {instance_ids}")
        return instance_ids

    except (BotoCoreError, ClientError) as error:
        print(f"Error stopping AWS instances: {error}")
        return []

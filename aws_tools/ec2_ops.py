import boto3
import time
from aws_tools import opsutil


def wait_ec2_system_status_ok(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    status = ''
    while status != 'ok':
        response = ec2.describe_instance_status(InstanceIds=[instance_id])
        status = opsutil.get_system_status_dict(response)['Status']
        time.sleep(10)


def wait_ec2_instance_running(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    ec2_inst_running_waiter = ec2.get_waiter('instance_running')
    ec2_inst_running_waiter.wait(InstanceIds=[instance_id])


def start_instance(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=[instance_id])


def stop_instances(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=[instance_id])


def is_running(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instance_status(InstanceIds=[instance_id])
    if 'InstanceStatuses' in response and len(response['InstanceStatuses']) == 0:
        return False
    return True





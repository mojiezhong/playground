#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2')

def get_instances():
    client = boto3.client('autoscaling')
    paginator = client.get_paginator('describe_auto_scaling_groups')
    groups = paginator.paginate().build_full_result()

    for asg in groups['AutoScalingGroups']:
        print asg['AutoScalingGroupName']


        instance_ids = [i for i in asg['Instances']]
        running_instances = ec2.instances.filter(Filters=[{}])
        for instance in running_instances:
            print(instance.id, instance.public_dns_name, instance.private_ip_address)

if __name__ == '__main__':
    get_instances()

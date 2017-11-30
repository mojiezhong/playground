#!/usr/bin/env python


from collections import defaultdict
import boto3

ec2 = boto3.resource('ec2')

def get_instances():
    client = boto3.client('elb')
    resp = client.describe_load_balancers(LoadBalancerNames=[
        'integration-routing',
    ])

    instance_ids = [i["InstanceId"] for i in resp['LoadBalancerDescriptions'][0]['Instances']]


    #running_instances = ec2.instances.filter(Filters=[{'Name':'InstanceId', 'Values':instance_ids}])
    running_instances = ec2.instances.filter(InstanceIds=instance_ids)
    with open("targets.json", "w") as f:

        targets = ""
        labels = ""
        for instance in running_instances:
            if len(targets) == 0:
                targets = '"{}:9990"'.format(instance.private_ip_address)
                labels = '"name":"{}"'.format(instance.public_dns_name)
            else:
                targets = targets + ',"{}:9990"'.format(instance.private_ip_address)
                labels = labels + ',"name":"{}"'.format(instance.public_dns_name)
            #print(instance.id, instance.public_dns_name, instance.private_ip_address)

        content = """
        [
          {{
            "targets":[{}],
            "labels": {{
              {}
            }}
          }}
        ]
        """.format(targets, labels)

        f.write(content)






if __name__ == '__main__':
    get_instances()

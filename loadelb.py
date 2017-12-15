#!/usr/bin/env python


from collections import defaultdict
import boto3
import time
import sys


loadbalances = [
    { 'profile':'ofpdev',
      'balance':'staging-routing',
     } ,
     {'profile':'ofpdev',
      'balance':'integration-routing',
      },
      {'profile':'prod',
      'balance':'prod-auth',
      },
      {'profile':'prod',
      'balance':'prod-routing',
      },
    ]

def get_instances():
    content = "["
    for lb in loadbalances:

        session = boto3.session.Session(profile_name=lb['profile'], region_name='us-east-1')
        client = session.client('elb')

        ec2 = session.resource('ec2')

        resp = client.describe_load_balancers(LoadBalancerNames=[lb['balance']])



        for lb in resp['LoadBalancerDescriptions']:
            instance_ids = [i["InstanceId"] for i in lb['Instances']]


            #running_instances = ec2.instances.filter(Filters=[{'Name':'InstanceId', 'Values':instance_ids}])
            running_instances = ec2.instances.filter(InstanceIds=instance_ids)



            for instance in running_instances:
                targets = '"{}:9990"'.format(instance.private_ip_address)
                labels = '"name":"{}","dns":"{}","instanceid":"{}"'.format(get_name(instance), instance.public_dns_name, instance._id)

                #print(instance.id, instance.public_dns_name, instance.private_ip_address)
                if content == "[" :
                        content += """
            {{
                "targets":[{}],
                "labels": {{
                  {}
                }}
            }}
                        """.format(targets, labels)
                else:
                        content += """
            ,{{
                "targets":[{}],
                "labels": {{
                  {}
                }}
              }}
            """.format(targets, labels)

    content += "]"

    with open("targets.json", "w") as f:
        f.write(content)



def get_name(instance):
    for dic in instance.tags:
        if dic["Key"] == "Name":
            return dic["Value"]

    return instance.public_dns_name


if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        print ("Pulling ......", i)
        try:
            get_instances()
        except Exception as ex:
            print ("Sleep ext 50s Got error ", ex)
            time.sleep(20)
        time.sleep(20)

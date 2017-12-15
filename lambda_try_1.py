# Dynamic DNS via AWS API Gateway, Lambda & Route 53
# Script variables use lower_case_
from __future__ import print_function

import json
import re
import hashlib
import boto3

print('Loading function <><><>><')


def lambda_handler(event, context):
    print(">>>> Gogogog")
    print("Received event: " + json.dumps(event, indent=2))

    print("context", context)
    # message = event['Records'][0]['Sns']['Message']
    # print(">>>>>>    From SNS: " + message)
    # print(">>>>>>    From event: " + event)
    return "message<><><>"

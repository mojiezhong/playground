#!/usr/bin/python
import re
import string
import random


s = '''

module "route53" {
  source = "../../../../deploy_config/terraform/route53/"
  service_name = "scout"
  # Pass outputs from elb module as variables
  aws_elb-service-dns_name = "${module.elb.aws_elb.service.dns_name}"
  aws_elb-service-zone_id = "${module.elb.aws_elb.service.zone_id}"
}

// Create DynamoDB table for scout topics
// Intended columns: <name>, <market_id>, <create_time>, <query>, <title> + index by market_id
resource "aws_dynamodb_table" "topics" {
  name           = "${terraform.env}_scout_topics"
  read_capacity  = "${terraform.env == "prod" ? 5 : 5}"
  write_capacity = "${terraform.env == "prod" ? 2 : 2}"
  hash_key       = "name"
  range_key      = "market_id"

  attribute {
    name = "name"
    type = "S"
  }

  attribute {
    name = "market_id"
    type = "S"
  }

  attribute {
    name = "create_time"
    type = "S"
  }




// Create DynamoDB table for scout topics
// Intended columns: <name>, <market_id>, <create_time>, <query>, <title> + index by market_id
resource "aws_dynamodb_table" "topics" {
  name           = "${terraform.env}_scout_topics"
  read_capacity  = "${terraform.env == "prod" ? 5 : 5}"
  write_capacity = "${terraform.env == "prod" ? 2 : 2}"
  hash_key       = "name"
  range_key      = "market_id"

  attribute {



// Create DynamoDB table for scout topics
// Intended columns: <name>, <market_id>, <create_time>, <query>, <title> + index by market_id
resource "aws_dynamodb_table" "topics" {
  name           = "${terraform.env}_scout_topics"
  read_capacity  = "${terraform.env == "prod" ? 5 : 5}"
  write_capacity = "${terraform.env == "prod" ? 2 : 2}"
  hash_key       = "name"
  range_key      = "market_id"

  attribute {



// Create DynamoDB table for scout topics
// Intended columns: <name>, <market_id>, <create_time>, <query>, <title> + index by market_id
resource "aws_dynamodb_table" "topics" {
  name           = "${terraform.env}_scout_topics"
  read_capacity  = "${terraform.env == "prod" ? 5 : 5}"
  write_capacity = "${terraform.env == "prod" ? 2 : 2}"
  hash_key       = "name"
  range_key      = "market_id"

  attribute {
'''


gs = re.findall(r'resource +"aws_dynamodb_table".*{(?: *\n)* *name.*=.*"(.*)"', s, re.M | re.I)



if  gs:
    for g in gs:
        print "find ====>>>", g

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"


for i in range(1, 20):
   x = "Deleting-" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
   print x


y = "testtest"

print len(y)

#print "indx", [1,2,3,4,5].index(9)

s = {1,2,3,4,5}

print s



s.add(10)

print s

print 15 in s

i = 0
while i < 10:
    #print i
    i = i + 2

print [[False] * 10] * 10

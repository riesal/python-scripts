# riesal[at]gmail[dot]com
import boto3
from botocore.exceptions import ClientError # try-catch in python

region = 'your-aws-region-id'
instances = ['your-instance-id1','your-instance-id2']
rds_instances = ['your-rds-instance-id1','your-rds-instance-id2']

def lambda_handler(event, context):
  ec2 = boto3.client('ec2', region_name=region)
  try:
      print 'Trying to stop all staging EC2 instances' + str(instances)
      ec2.stop_instances(InstanceIds=instances)
  except ClientError as error:
      print 'Sorry, can not find some of instances, stopping aborted.'

  rds_conn = boto3.client('rds',region_name=region)
  for stg in rds_instances:
      try:
          print 'Trying to stop RDS instance of ' + str(stg)
          rds_conn.stop_db_instance(DBInstanceIdentifier=stg)
      except ClientError as error:
          print 'Sorry, i can not find RDS instance of ' + str(stg)

  print 'all of rds staging instances was stopped.'

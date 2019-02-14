# finaccel
# cd /tmp && virtualenv tes
# source /tmp/tes/bin/activate
# pip install boto3 awspolicy

import boto3
import awspolicy
from awspolicy import BucketPolicy

def list()
  s3 = boto3.client('s3')
  response = s3.list_buckets()
  buckets = [bucket['Name'] for bucket in response['Buckets']]
  print("The bucket list: %s" % buckets)

def create()
  s3 = boto3.client('S3')
  response = s3.create_bucket(Bucket='my-bucket')

def delete()
  s3 = boto3.client('S3')
  response = s3.delete_bucket(Bucket='my-bucket')

def grant()
  # define user arn dan bucket name
  user_arn_ku = 'arn:aws:iam::88888888:/user/your_username'
  bucket_name = 'my-bucket'

  # connect dan set policy
  s3 = boto3.client('S3')
  bucket_policy = BucketPolicy(serviceModule=s3_client, resourceIdentifer=bucket_name)
  ganti_permission = bucket_policy.select_statement('AutomatedRestrictiveAccess')

  # append dan save user
  ganti_permission.Principal['AWS'].append(user_arn_ku)
  ganti_permission.save()
  ganti_permission.source_policy.save()

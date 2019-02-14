#!/tmp/tes/bin/python
# using python 2.7
# finaccel
# cd /tmp && virtualenv tes
# source /tmp/tes/bin/activate
# pip install boto3 awspolicy

import os, sys, getopt, argparse
import boto3
import awspolicy
from awspolicy import BucketPolicy

AWS_DEFAULT_REGION = 'ap-southeast-1'
os.environ['AWS_DEFAULT_REGION'] = 'ap-southeast-1'

def list_bucket():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("The bucket list: %s" % buckets)

def create_bucket():
    bucket_name = str(sys.argv[2])
    #print "Bucket name is: ", bucket_name
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION})

def delete_bucket():
    bucket_name = str(sys.argv[2])
    #print "Bucket name is: ", bucket_name
    s3 = boto3.client('s3')
    response = s3.delete_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION})

def grant_user():
    # define user arn dan bucket name
    user_arn_ku = str(sys.argv[2]) #user_arn_ku = 'arn:aws:iam::88888888:/user/your_username'
    bucket_name = str(sys.argv[3]) #bucket_name = 'my-bucket'

    # connect bucket
    s3 = boto3.client('s3')
    bucket_policy = BucketPolicy(serviceModule=s3_client, resourceIdentifer=bucket_name)
    ganti_permission = bucket_policy.select_statement('AutomatedRestrictiveAccess')

    # append dan save bucket policy
    ganti_permission.Principal['AWS'].append(user_arn_ku)
    ganti_permission.save()
    ganti_permission.source_policy.save()

def revoke_user():
    # define user arn dan bucket name
    user_arn_ku = str(sys.argv[2]) #user_arn_ku = 'arn:aws:iam::88888888:/user/your_username'
    bucket_name = str(sys.argv[3]) #bucket_name = 'my-bucket'

    # connect bucket
    s3 = boto3.client('s3')
    bucket_policy = BucketPolicy(serviceModule=s3_client, resourceIdentifer=bucket_name)
    ganti_permission = bucket_policy.select_statement('AutomatedRestrictiveAccess')

    # revoke dan save bucket policy
    ganti_permission.Principal['AWS'].delete(user_arn_ku)
    ganti_permission.save()
    ganti_permission.source_policy.save()

# rencana pakai function_map dan parser tapi belum di test.
# function_map = { 'list': list_bucket, 'create': create_bucket, 'delete': delete_bucket, 'grant': grant_user, 'revoke': revoke_user }
# parser = argparse.ArgumentParser() parser.add_argument('command', nargs=1) parser.add_argument('--args', nargs='+') args = parser.parse_args() function = function_map[args.command[0]] if args.args: function(args.args) else: function()

if __name__ == "__main__":
    print "Number of arguments:", len(sys.argv), "arguments."
    print "Argument list:", str(sys.argv)
    print "\n"

    if "list" in str(sys.argv[1]):
        list_bucket()
        sys.exit()
    elif "create" in str(sys.argv[1]):
        create_bucket()
        sys.exit()
    elif "delete" in str(sys.argv[1]):
        delete_bucket()
        sys.exit()
    elif "grant" in str(sys.argv[1]):
        grant_user()
        sys.exit()
    elif "revoke" in str(sys.argv[1]):
        revoke_user()
        sys.exit()

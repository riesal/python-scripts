# riesal[at]gmail[dot]com
import boto3
region = 'your-aws-region-id'
instances = ['your-instance-id1','your-instance-id2']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'stopped your instances: ' + str(instances)

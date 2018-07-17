from  future_ import print_function
import boto3, json, re

region = 'your-aws-ec2-region'
route53 = boto3.client('route53')
ec2 = boto3.resource('ec2')

def add_cname_record(mesin,nama):
    instances = ec2.Instance(mesin)
    instances_dns = instances.public_dns_name

    route53.change_resource_record_sets(
        HostedZoneId='your-aws-route53-id',
	    ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
		            'ResourceRecordSet': {
                        'Name': nama,
		                'Type': 'CNAME',
		                'ResourceRecords': [
                            {
		                        'Value': instances_dns
                            }
                        ],
                        'TTL':  60
                    }     
                }
            ]
        }
    )

def lambda_handler(event, context):
    mesins = {
        'your-instance-id1': 'your1-fqdn.com.',
        'your-instance-id2': 'your2-fqdn.com.'
    }

    for mesin, nama in mesins.items():
        add_cname_record(mesin, nama)

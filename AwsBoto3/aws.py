import boto3
import json

s3 = boto3.resource('s3');

for bucket in s3.buckets.all():
    print(bucket)


EC2 = boto3.resource("ec2")
instances = EC2.instances.all()

for instance in instances:
    print(instance.id)
    print(instance.state)
    print(instance.image.id)
    print(instance.instance_type)
    print(instance.public_ip_address)



Iam = boto3.client('iam')

IamAllUsers = Iam.list_users()

ListOfUsers = []

for user in IamAllUsers['Users']:
    ListOfUsers.append(user)
    

print(ListOfUsers)
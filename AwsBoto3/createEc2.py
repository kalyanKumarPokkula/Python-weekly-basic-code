import boto3

ec2 = boto3.resource('ec2')

instancesParams = {
    'ImageId' : 'ami-0287a05f0ef0e9d9a',
    'MaxCount' : 1,
    'MinCount' : 1,
    'InstanceType' : 't2.micro',
    'KeyName' : 'AWS_LOGIN',
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'test2-ansible'
                },
                # Add other tags as needed
            ]
        }
    ]
}

def create_ec2_instances(instance_params):
    try:
        instance = ec2.create_instances(**instance_params)
        print("Instance created Successfully")
        print(instance)
    except Exception as e:
        print(e)
    


create_ec2_instances(instancesParams)


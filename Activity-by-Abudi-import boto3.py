import boto3

def launch_instances(image_id, region):
    # Create a connection to the EC2 service
    ec2 = boto3.client('ec2', region_name=region)
    
    # Launch an EC2 instance in the specified region
    instance_response = ec2.run_instances(
        ImageId=image_id,
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
    )
    instance_id = instance_response['Instances'][0]['InstanceId']
    print(f"Launched instance {instance_id} in {region}")
    
    # Launch an EC2 instance in a different region
    other_region = 'us-west-2' if region == 'us-east-1' else 'us-east-1'
    ec2_other_region = boto3.client('ec2', region_name=other_region)
    instance_response = ec2_other_region.run_instances(
        ImageId=image_id,
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
    )
    instance_id = instance_response['Instances'][0]['InstanceId']
    print(f"Launched instance {instance_id} in {other_region}")

#This function uses the boto3 library to interact with the Amazon Web Services (AWS) SDK for Python to launch EC2 instances. The run_instances method is used to start EC2 instances with the specified ImageId and InstanceType.

#The function takes two arguments: image_id is the ID of the Amazon Machine Image (AMI) to launch the EC2 instance with, and region is the AWS region where the first instance should be launched.

#The function first creates a connection to the EC2 service in the specified region using the boto3.client method. It then launches an EC2 instance in the specified region using the run_instances method, and prints the instance ID and the region where the instance was launched.

#The function then launches another EC2 instance in a different region (us-west-2 if the first region was us-east-1, or us-east-1 if the first region was us-west-2). It creates a new connection to the EC2 service in the other region using boto3.client and launches an EC2 instance using run_instances, and prints the instance ID and the region where the instance was launched.
import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection and set the region
ec2 = boto3.resource('ec2', region_name='ap-southeast-1')

def lambda_handler(event, context):

    # all running EC2 instances.
    filters = [{
            'Name': 'tag:AutoStop',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    #filter the instances which are stopped
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    RunningInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    #print RunningInstances 
    
    if len(RunningInstances) > 0:
        #perform the shutdown
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print(shuttingDown)
    else:
        print("Nothing to see here")


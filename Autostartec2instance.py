import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2', region_name='ap-south-1')

def lambda_handler(event, context):

    # all stopped EC2 instances.
    filters = [{
            'Name': 'tag:AutoStart',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all stopped instances
    RunningInstances = [instance.id for instance in instances]
    

    #print StoppedInstances 
    
    if len(RunningInstances) > 0:
        #perform the startup
        AutoStarting = ec2.instances.filter(InstanceIds=RunningInstances).start()
        print(AutoStarting)
    else:
        print("Nothing to see here")


Lambda script and steps  for ec2 stop and start at specific time Based on tags

1.Create a custom AWS IAM policy and execution role for  Lambda function.



#Create a iam role with this policy


Tagging Instances

Note: Tag all the instance which need to be auto stop and auto start. 

Region = ap-southeast-1 
Name = AutoStart ; Value = True (To start the instances)
Name = AutoStop ; Value = True (To stop the instances)

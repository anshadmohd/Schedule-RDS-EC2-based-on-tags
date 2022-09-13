Lambda script and steps  for ec2 stop and start at specific time Based on tags

1.Create a custom AWS IAM policy and execution role for  Lambda function.


#Create a iam role with this policy


Tagging Instances

Note: Tag all the instance which need to be auto stop and auto start. 

Region = region_name
Name = AutoStart ; Value = True (To start the instances)
Name = AutoStop ; Value = True (To stop the instances)

#Create Lambda functions that stop and start your EC2 instances

1.    In the AWS Lambda console, choose Create function.
2.    Choose Author from scratch.
3.    Under Basic information, add the following:
*For Function name, enter a name that identifies it as the function used to stop your EC2 instances. For example, "StopEC2Instances".
*For Runtime, choose Python 3.7.
*Under Permissions, expand Change default execution role.
*Under Execution role, choose Use an existing role.
*Under Existing role, choose the IAM role that you created.
4.    Choose Create function.
5.    Under Code, Code source, copy and paste the following code into the editor pane in the code editor (Autostopec2instance.py). This code stops the EC2 instances that you identify.
6.    Choose Deploy.
7.    On the Configuration tab, choose General configuration, Edit. Set Timeout to 10 seconds and then select Save.
Note: Configure the Lambda function settings as needed for your use case. For example, if you want to stop and start multiple instances, you might need a different value for Timeout and Memory.
8.    Repeat steps 1-7 to create another function. Do the following differently so that this function starts your EC2 instances:
In step 5
(use Autostartec2instance.py)


Test your Lambda functions

1.    In the AWS Lambda console, choose Functions.
2.    Choose one of the functions that you created.
3.    Select the Code tab.
4.    In the Code source section, select Test.
5.    In the Configure test event dialog box, choose Create new test event.
6.    Enter an Event name. Then, choose Create.
Note: You don't need to change the JSON code for the test event—the function doesn't use it.
7.    Choose Test to run the function.
8.    Repeat steps 1-6 for the other function that you created.


Create EventBridge rules that trigger your Lambda functions

1.    Open the Eventbridge console.cloudwatch
2.    Select Create rule.
3.    Enter a Name for your rule, such as "StopEC2Instances". You can optionally enter a Description.
 
4.    In Define pattern, select Schedule.
5.For Cron expression, enter an expression that tells Lambda when to stop your instances
6.    In Select targets, choose Lambda function from the Target drop-down menu.
7.   For Function, choose the function that start your EC2 instances.
8.    Scroll down and then select Create.
9.  create another rule for stop instance repeat step 2-8
In step 7 chose the function that stops your ec2 instance


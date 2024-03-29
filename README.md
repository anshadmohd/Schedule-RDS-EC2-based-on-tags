Lambda script and steps  for EC2&RDS stop and start at specific time Based on tags




## STEPS

## 1.Create a custom AWS IAM policy and execution role for  Lambda function(chose iampolicy).


#Create a iam role with this policy


## Tagging Instances

Note: Tag all the instance which need to be auto stop and auto start. 

Region = region_name
Name = AutoStart ; Value = True (To start the instances)
Name = AutoStop ; Value = True (To stop the instances)

## Create Lambda functions that stop and start your EC2 instances

1.    In the AWS Lambda console, choose Create function.
2.    Choose Author from scratch.
3.    Under Basic information, add the following:
* For Function name, enter a name that identifies it as the function used to stop your EC2 instances. For example, "StopEC2Instances".
* For Runtime, choose Python 3.7.
* Under Permissions, expand Change default execution role.
* Under Execution role, choose Use an existing role.
* Under Existing role, choose the IAM role that you created.
5.  Choose Create function.
6.    Under Code, Code source, copy and paste the following code into the editor pane in the code editor (Autostopec2instance.py). This code stops the EC2 instances that you identify.
7.    Choose Deploy.
8.    On the Configuration tab, choose General configuration, Edit. Set Timeout to 10 seconds and then select Save.
Note: Configure the Lambda function settings as needed for your use case. For example, if you want to stop and start multiple instances, you might need a different value for Timeout and Memory.
 Repeat steps 1-7 to create another function. Do the following differently so that this function starts your EC2 instances:
In step 5
(use Autostartec2instance.py)


## Test your Lambda functions

1.    In the AWS Lambda console, choose Functions.
2.    Choose one of the functions that you created.
3.    Select the Code tab.
4.    In the Code source section, select Test.
5.    In the Configure test event dialog box, choose Create new test event.
6.    Enter an Event name. Then, choose Create.
Note: You don't need to change the JSON code for the test event—the function doesn't use it.
7.    Choose Test to run the function.
8.    Repeat steps 1-6 for the other function that you created.


## Create EventBridge rules that trigger your Lambda functions

1.    Open the Eventbridge console.cloudwatch
2.    Select Create rule.
3.    Enter a Name for your rule, such as "StopEC2Instances". You can optionally enter a Description.
 
4.   In Define pattern, select Schedule.
5.   For Cron expression, enter an expression that tells Lambda when to stop your instances
6.   In Select targets, choose Lambda function from the Target drop-down menu.
7.   For Function, choose the function that start your EC2 instances.
8.   Scroll down and then select Create.
9.   create another rule for stop instance repeat step 2-8
In step 7 chose the function that stops your ec2 instance

# Schedule Amazon RDS stop and start using AWS Lambda 

1.Create a iam role with rdsiampolicy

2.Add  tags to rds

* Open the Amazon RDS Console.
* In the navigation pane, Choose Databases.
* Choose the DB instance that you want to start and stop automatically.
* In the details section, scroll down to the Tags section.
* Under the Tags tab, choose Add. For Tag key, enter AutoStart. For Value, enter true. Choose Add to save your changes.
* Choose Add again. For Tag key, enter AutoStop. For Value, enter True. Choose Add to save your changes


3.Open the Amazon RDS Console.

In the navigation pane, Choose Databases.
Choose the DB instance that you want to start and stop automatically.
In the details section, scroll down to the Tags section.
Under the Tags tab, choose Add. For Tag key, enter AutoStart. For Value, enter true. Choose Add to save your changes.
Choose Add again. For Tag key, enter AutoStop. For Value, enter True. Choose Add to save your changes.
Create a Lambda function to start the tagged DB instances
1.    Open the Lambda Console.
2.    In the navigation pane, choose Functions.
3.    Choose Create function.
4.    Choose Author from scratch.
5.    For Function name, enter the name of your function.

6.    For Runtime, select Python 3.9.
7.    For Architecture, leave the default selection of x86_64.
7.    Expand Change default execution role.
8.    For Execution role, select Use an existing role.
1.Create a custom AWS IAM policy and execution role for  Lambda function(chose iampolicy).
9
9.    For Existing role, select the IAM role that you created earlier.
10.    Choose Create function.
11.    Choose the Code tab.
12.    In the Code source editor, delete the sample code and paste the AutostartRDS.py

13.    Choose File, choose Save, and then choose Deploy.
15.    Choose the Configuration tab, choose General configuration, and then choose Edit.
16.    Under Timeout, do the following: For min, select 0. For sec, select 10. 17.    Choose Save.

Create a Lambda function to stop the tagged DB instances(select AutostopRDS.py)

# Perform function testing

* Suppose that your tagged DB instances are in the Stopped state. To perform function testing, do the following:
* Open the Lambda Functions list.
* Choose the function that you created to start the DB instances .
* Choose Actions, and then choose Test.
* Under the Test tab, for Name, enter the name of your event.
* Choose Save changes, and then choose Test.
* Open the Lambda Functions list.

# Create the schedule

* Choose the function that you created to start the DB instances.
* Under Function overview, choose Add trigger.
* Select EventBridge (CloudWatch Events), and then select Create a new rule.
* For Rule name, enter the name of the rule that you want to create.
* For Schedule Expression, add a cron expression for the automated schedule

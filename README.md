# aws-snapshots-automation
AWS EC2 Snapshots Automation

# about
This project is a demo. It uses boto3 to manage AWS EC2 Instance snapshots

# Configuring
shotty uses the configuration file created by the AWS CLI.
Example:
'aws configure -profile shotty'

# Running
'pipenv run "python shotty/shotty.py <command> <--project=PROJECT>"'

*command* is list, start, or stop
*project* is optional

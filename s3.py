import boto3
import json

s3= boto3.client('s3')
print(s3)

def lambda_handler(event, context);
    bucket = event['Records'][0]['s3']['bucket']['name']

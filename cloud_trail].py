import boto3

client = boto3.client('cloudtrail')
response = client.describe_trails()

aa = response['trailList'][0]['S3BucketName']
eve_logs = client.get_event_selectors(
    TrailName='security'
)
print(eve_logs)
#print(response)
#response['trailList'][0]['S3BucketName']
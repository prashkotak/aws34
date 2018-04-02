import boto3

BUCKET = "jobanjola"
KEY = "LOL/SOME/KEY"

client = boto3.client("s3")

result = client.get_object(Bucket=BUCKET, Key=KEY)

# Read the object (not compressed):
text = result["Body"].read().decode()

print(text)
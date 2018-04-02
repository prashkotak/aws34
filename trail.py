import boto3
import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

client = boto3.client('cloudtrail')

response = client.describe_trails()
print(response)
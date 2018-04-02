# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)
#
import datetime
now = datetime.datetime.now()

import boto3
import os, errno
import botocore
import gzip
import json

S3KeyPrefix='AWSLogs/594842924673/CloudTrail/us-west-2/2018/03/07'
S3Bucket='deepsecuritylog'
store_path='C:\\Users\\Darpan\\Desktop\\logfile\\'

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
response = s3.list_objects_v2(
    Bucket=S3Bucket,
    Prefix=S3KeyPrefix
)
rpt = ''
for obj in response['Contents']:
    object_key = obj['Key']
    print('Key: '+object_key)
    file_path = store_path+object_key;
    folder_path = file_path[0:file_path.rfind('/')]
    if not os.path.exists(folder_path):
       os.makedirs(folder_path)
    s3_new = session.resource('s3')
    s3_new.meta.client.download_file(S3Bucket, object_key, file_path);

    # with gzip.open(file_path, "rb") as f:
    #     d = json.loads(f.read().decode("ascii"))
    #     for nik in d['Records']:
    #        #print(nik['eventName'])
    #         if nik['eventName'] == 'RunInstances':
    #             print("aaaaa")





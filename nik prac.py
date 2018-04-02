# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)
#
# import datetime
# now = datetime.datetime.now()
# print(now.
import boto3
import os, errno
import botocore
import gzip
import json
#og/AWSLogs/554906049655/CloudTrail/us-east-1/2018/03/06/554906049655_CloudTrail_us-east-1_20180306T0640Z_9yNIXKqYIVznl2sf.json.gz

S3KeyPrefix='log/AWSLogs/554906049655/CloudTrail/us-east-1/'
S3Bucket='jobanjola'
store_path='C:\\Users\\Darpan\\Desktop\\tmp33\\'

session = boto3.Session(profile_name='demo')
s3 = session.client('s3')
response = s3.list_objects_v2(
    Bucket=S3Bucket,
    Prefix=S3KeyPrefix
)


for obj in response['Contents']:
    object_key = obj['Key']

    print('Key: '+object_key)

    file_path = store_path+object_key;
    folder_path = file_path[0:file_path.rfind('/')]

    #print('File path: ' + file_path)
    #print('Folder path: ' + folder_path)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    s3_new = session.resource('s3')
    s3_new.meta.client.download_file(S3Bucket, object_key, file_path);

    with gzip.open(file_path, "rb") as f:
        d = json.loads(f.read().decode("ascii"))
        print(d)

    if object_key in obj.key:
        content = obj.get()['Body'].read()
        #og/AWSLogs/554906049655/CloudTrail/us-east-1/2018/03/06/554906049655_CloudTrail_us-east-1_20180306T0640Z_9yNIXKqYIVznl2sf.json.gz
        aa = bucket._name +"/"+ obj.key
        with gzip.open(aa, "rb") as f:
         d = json.loads(f.read().decode("ascii"))
         print(d)

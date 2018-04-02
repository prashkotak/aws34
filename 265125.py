from datetime import datetime, timedelta
import boto3
import os
import json
import  gzip


today = datetime.now()
startdate = today - timedelta(days=1)
enddate = today.date()
std = startdate.date()
end = enddate

import datetime
S3Bucket = 'cloudtrail-deep'
store_path = 'C:\\Users\\Darpan\\Desktop\\tmp81\\'



start = datetime.datetime.strptime(str(std), "%Y-%m-%d")
end = datetime.datetime.strptime(str(end), "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
console_login = 'User Login ' + "\n"
for datex in date_generated:
    print(datex.strftime("%d-%m-%Y"))
    S3KeyPrefix = 'AWSLogs/594842924673/CloudTrail/us-west-2'+ "/" + datex.strftime("%Y")  + "/" + datex.strftime("%m")+ "/" + datex.strftime("%d")+"/"
    #S3KeyPrefix = 'log/AWSLogs/594842924673/CloudTrail/us-west-2/'
    session = boto3.Session(profile_name='default')
    s3 = session.client('s3')
    response = s3.list_objects_v2(
    Bucket = S3Bucket,
    Prefix = S3KeyPrefix
    )
    for obj in response['Contents']:
      object_key = obj['Key']
      file_path = store_path + object_key;
      folder_path = file_path[0:file_path.rfind('/')]
      if not os.path.exists(folder_path):
        os.makedirs(folder_path)
      s3_new = session.resource('s3')
      s3_new.meta.client.download_file(S3Bucket, object_key, file_path);

      # with gzip.open(file_path, "rb") as f:
      #    d = json.loads(f.read().decode("ascii"))
      #    for nik in d['Records']:
      #       #print(nik['eventName'])
      #        if nik['eventName'] == 'ConsoleLogin':
      #            #console_login = console_login + userName
      #
      #            print("aaaaa")
      #            xx= input()








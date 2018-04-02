import os
import gzip
import json
from datetime import datetime, timedelta
import datetime

date_range_days = 7
snap_start_date = datetime.now() - timedelta(days=date_range_days)



def Header(head):
    header = ''
    header = header + '='.center(70,'=')   +"\n" # +"<br>"
    header = header +repr(head).center(70) +"\n" #+ "<br>"
    header = header + '='.center(70,'=')   + "\n"#+"<br>"
    return  header


direc = 'C:\\Users\Darpan\\Desktop\\logfile\AWSLogs\\594842924673\\CloudTrail\\us-west-2\\2018\\03\\07'

#head = Header('Instance created ')

for root, dirs, files in os.walk(direc):
    for filename in files:
        file_path = str(direc) +"\\" + str(filename)
        #print(file_path)
        with gzip.open(file_path, "rb") as f:
             d = json.loads(f.read().decode("ascii"))
             for nik in d['Records']:
                 # print(nik['eventName'])
                 abc = nik['eventName']
                 if abc == 'DescribeInstances':
                     print(nik['sourceIPAddress'])
                 # else :
                 #     print("false")



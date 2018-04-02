import boto3
import datetime
import gzip
import json
import glob
import os


#name = "C:\\Users\\Darpan\\Desktop\\tmp75\\AWSLogs\\594842924673\\CloudTrail\\us-west-2\\"
#name = "C:/Users/Darpan/Desktop/tmp75/AWSLogs/594842924673/CloudTrail/us-west-2/"

def scanfolder():
    console_login = 'User Login details'+"\n"
    create_instance ='Instance create details'+"\n"
    count  = 0
    acpath ='C:/Users/Darpan/Desktop/tmp76\AWSLogs/594842924673/CloudTrail/us-west-2'
    #for path, dirs, files in os.walk('C:/Users/Darpan/Desktop/tmp75/AWSLogs/594842924673/CloudTrail/us-west-2'):
    for path, dirs, files in os.walk(acpath):
        for d in dirs:
            for file_path in glob.iglob(os.path.join(path, d, '*.gz')):
                count = count + 1
                with gzip.open(file_path, "rb") as f:
                  d = json.loads(f.read().decode("ascii"))
                  for nik in d['Records']:
                   #print(nik['eventName'])
                   if nik['eventName'] == "ConsoleLogin":
                       console_login = console_login + nik['userIdentity']['userName'] + "  " + nik['sourceIPAddress'] + "\n"
                   if nik['eventName'] == 'RunInstances':
                      print("Filer read ", count)
                      create_instance = create_instance + nik['userIdentity']['userName'] +" "+ nik['requestParameters']['instanceType']

                     #console_login = console_login +nik['userIdentity']['userName'] + "  "+ nik['sourceIPAddress'] +"\n"

    print(console_login)
    print(create_instance)

scanfolder()

















#print(os.listdir(file_path))


#print(glob.glob("C:\Users\Darpan\Desktop\tmp75\AWSLogs\594842924673\CloudTrail\us-west-2\*.json"))


 # with gzip.open(file_path, "rb") as f:
 #    d = json.loads(f.read().decode("ascii"))
 #    for nik in d['Records']:
 #       #print(nik['eventName'])
 #        if nik['eventName'] == 'ConsoleLogin':
 #            #console_login = console_login + userName
 #            print("aaaaa")
 #            xx= input()
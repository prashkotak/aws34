import boto3
from datetime import datetime, timedelta
today1 = datetime.now()
tdy = str(today1.date())
std =today1- timedelta(days=1)
std  = str(std.date())
client = boto3.client('guardduty')
response = client.list_findings(
        DetectorId='a2b0a39871e32176049db785d52154b3',
       )
findings = list();
for find_id in response['FindingIds']:
         findings.append(find_id)
lsrpt='Low severity '+ "\n"
msrpt='Mediun Severity'+ "\n"
hsrpt='High Severity'+ "\n"
ls = 0
ms = 0
hs = 0
for get_id in findings:
 res = client.get_findings(
    DetectorId='a2b0a39871e32176049db785d52154b3',
    FindingIds=([get_id]))
 for nik in res['Findings']:
   if tdy in nik['Service']['EventLastSeen'] or std in nik['Service']['EventLastSeen']:

       if float(nik['Severity']) == 2.0:
          #print("Low severity")
          ls = ls + 1

          lsrpt = lsrpt +str.replace(str(nik['Service']['EventLastSeen']),"T"," ")+"   "+nik['Title'] + "\n"
       elif float(nik['Severity']) == 5.0:
          #print("Medium severity")
          ms = ms + 1
          msrpt = msrpt + str.replace(str(nik['Service']['EventLastSeen']),"T"," ")+"   "+nik['Title'] + "\n"
       else:
          #print("High Severity")
          hsrpt = hsrpt + str.replace(str(nik['Service']['EventLastSeen']),"T"," ")+"   "+nik['Title'] + "\n"
          hs = hs + 1
rptcnt = False
rpt = ""
if ls > 0:
    rpt = rpt + lsrpt
    rptcnt = True
if hs > 0:
    rpt = rpt + hsrpt
    rptcnt = True
if ms > 0:
    rpt = rpt + msrpt
    rptcnt = True
if rptcnt == True:
    client = boto3.client('sns')
    client.publish(Message="Guard Duty: " + str(rpt) + "\n", TopicArn="arn:aws:sns:us-west-2:594842924673:APTDBServer")



# res['Findings'][0]['Service']['Action']['ActionType']

# print(get_id)
#nik['Description']
#nik['Severity'] = '2.0'
#res['Findings'][0]['Service']['EventLastSeen']
#res['Findings'][0]['Title']
#nik['Service']['EventLastSeen']


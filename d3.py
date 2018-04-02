import datetime
from datetime import date, timedelta
def find_cost(desc,stdt,endt):
    import boto3
    client = boto3.client('ce')
    stdt = str(stdt)
    endt = str(endt)
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': stdt,
            'End': endt
        },
        Granularity='DAILY',
        Metrics=[
            'BlendedCost',
        ],
    )
    bill = 0
    for nik in response['ResultsByTime']:
        amt = float(nik['Total']['BlendedCost']['Amount'])
        bill = bill + amt
    # print(desc)
    # print(bill)
    rpt = str(round(bill))
    return rpt + " $"

def Last_five_cost(stdt, endt):
        import boto3
        client = boto3.client('ce')
        stdt = str(stdt)
        endt = str(endt)
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': stdt,
                'End': endt
            },
            Granularity='DAILY',
            Metrics=[
                'BlendedCost',
            ],
        )
        bill = str(stdt)
        for nik in response['ResultsByTime']:
            amt = round(float(nik['Total']['BlendedCost']['Amount']),2)
            bill = bill +"   " +str(round(amt)) +" $"
        #print(bill)
        return bill

rptfinal = ""
tommrw = date.today() + timedelta(1)
yesterday = date.today() - timedelta(1)
daybeforyesterday = date.today() - timedelta(2)
tday = datetime.date.today()
todayDate = datetime.date.today()
if (todayDate - todayDate.replace(day=1)).days > 25:
    stmonth= todayDate + datetime.timedelta(30)
    stmonth.replace(day=1)
    # print(stmonth)
else:
    stmonth = (todayDate.replace(day=1))
last_days = tday.day
desc0 =  "Bills inscreased in Last Ten Days"+"\n"
rptfinal = rptfinal + str(desc0)
for i in range(1,last_days):
    stdt = date.today() - timedelta(i)
    endt = date.today() - timedelta(i-1)
    rpt0 = Last_five_cost(stdt,endt)
    rptfinal = rptfinal + str(rpt0)+"\n"

# desc1=""
# desc1 ='\033[1m'+  "BILL TILL YESTERDAY  "+ str(stmonth) + " to " + str(yesterday) + ":"+'\033[0m' +"\n"
# rpt1 = find_cost(desc1,stmonth,yesterday)
# rptfinal =rptfinal + str(desc1)+""+str(rpt1)+ "\n"


desc2=""
desc2 ="MTD:         "
rpt2 = find_cost(desc2,stmonth,tommrw)

rptfinal = rptfinal + str(desc2)+str(rpt2)+"\n"
import boto3
client = boto3.client('sns')
#client.publish(Message="Aws Billing  " + str(rptfinal) + "\n", TopicArn="arn:aws:sns:us-west-2:594842924673:APTDBServer")
#client.publish(Message="Aws Billing  " + str(rptfinal) + "\n", TopicArn="arn:aws:sns:us-west-2:594842924673:Alarm_SMS")
print(rptfinal)





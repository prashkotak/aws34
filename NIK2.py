import datetime
#from d3 import find_cost
from datetime import date, timedelta


def find_cost1(desc,stdt,endt):
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
    ##print(desc)
    print(bill)


last_days = 6
desc1 = "BILL INSCREASE IN LAST 5 DAYS  "+ "\n"
for i in range(1,last_days):
    stdt = date.today() - timedelta(i)
    endt = date.today() - timedelta(i-1)
    #print(str(stdt) +" "+ str(endt))
    desc1=""
    desc1= str(stdt) + ":"
    find_cost1(desc1,stdt,endt)



# if (todayDate - todayDate.replace(day=1)).days > 25:
#     stmonth= todayDate + datetime.timedelta(30)
#     stmonth.replace(day=1)
#     print(stmonth)
# else:
#     stmonth = (todayDate.replace(day=1))
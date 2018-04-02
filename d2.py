import datetime
from datetime import date, timedelta


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

print(stmonth.day )
print(tday.day)


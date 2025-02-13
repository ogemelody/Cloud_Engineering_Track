"""import datetime
#using datetime.time
t= datetime.time(9,13,000)
print(t.hour)
#using datetime.date
t = datetime.date(2003,4,13)
print(t.year)
#combime the both - datetime
dt = datetime.datetime(2016,5,29,12,30,45,10000)
tdelta = datetime.timedelta(days =7)
print(dt + tdelta)

#still learn about various timezone
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

#strftime method--convert from datetime to string
print(dt.strftime("%B, %d, %Y"))

#CONVERT FRM STRING TO DATE TIME - strptime
dt_str = "May 24, 2009"
dt_t = datetime.datetime.strptime(dt_str,"%B %d, %Y" )
print(dt_t)
#strftime and strptime is for formating not for calculation
#strftime - DATETIME TO STRING
#strptime - STRING TO DATETIME

import datetime
lee_birthdate = datetime.datetime(2001, 7, 4, 14, 30)
current_time = datetime.datetime.now()
time_difference= current_time - lee_birthdate
seconds = time_difference.total_seconds() #USE total_seconds as it calc the total seconds as strftime("%S") wont work as it only format
hours = int(seconds // 3600)
print(f"{hours} hours since Lee was born.")


lee_birth = datetime.datetime(2001, 7, 4)
weekday = lee_birth.strftime("%A")
print(weekday)"""
print(1/2+3//3+4**2)
#print(20.12*10^8)
print(1/1)
z = y = x =1
print(x,y,z, sep = "*")
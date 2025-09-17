import datetime as dt
now = dt.datetime.now()
print(now)
print(type(now))
year = now.year
month = now.month
day = now.day
week_day = now.weekday()

date_of_birth = dt.datetime(year=1996, month=8, day=20)
print(date_of_birth)
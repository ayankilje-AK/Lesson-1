from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("The time now is", now)

print("The date components:", today.day, today.month, today.year)
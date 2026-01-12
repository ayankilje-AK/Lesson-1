import random
import time

def getRandomDate(start_date, end_date):
    print(f"We are printing random dates between {start_date} and the {end_date}")
    random_generator = random.random()
    date_format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))
    random_time = start_time + random_generator * (end_time - start_time) 
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date

print("Random Date =", getRandomDate("01/01/2016", "12/12/2018"))

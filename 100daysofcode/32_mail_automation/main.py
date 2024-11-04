import smtplib
import settings
import datetime as dt
import random


now = dt.datetime.now()
year = now.year
day_of_the_week = now.weekday()

with open('quotes.txt','r') as data:
    content = data.read().split('\n')
    quote_of_the_day = content[random.randint(0, len(content)-1)]
    
if day_of_the_week == 1:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=settings.my_email, password=settings.password)
        connection.sendmail(
            from_addr=settings.my_email, 
            to_addrs="jrokcode@gmail.com", 
            msg=f"Subject: Quote of the day\n\n{quote_of_the_day}"
            )
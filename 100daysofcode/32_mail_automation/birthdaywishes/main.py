##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_date = dt.datetime.now()
todays_month = today_date.month
todays_day = today_date.day



print(todays_month)
data = pd.read_csv('birthdays.csv')
print(data["month"])


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





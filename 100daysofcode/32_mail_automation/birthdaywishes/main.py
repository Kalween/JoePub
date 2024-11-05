##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib
import settings
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_date = dt.datetime.now()
todays_month = today_date.month
todays_day = today_date.day
print(todays_day)


# Läs in CSV-filen
data = pd.read_csv('birthdays.csv')

# Filtrera rader där både månad och dag matchar dagens datum
today_birthdays = data[(data['month'] == todays_month) & (data['day'] == todays_day)]

# Om vi hittar några matcher, printa deras namn
if not today_birthdays.empty:
    birthday_hen = (today_birthdays['name'].tolist())
else:
    print("Ingen har födelsedag idag.")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letters = './letter_templates/letter_'

# Om vi hittar några matcher, iterera över dem och skicka ett meddelande till varje
if not today_birthdays.empty:
    for index, row in today_birthdays.iterrows():
        person_name = row['name']
        person_email = row['email']  # Antar att din CSV har en 'email'-kolumn
        # Läser in en slumpmässig brevmall
        with open(f'{letters}{random.randint(1,3)}.txt') as file:
            letter = file.read()
            # Anpassa brevet med personens namn
            personalized_letter = letter.replace('[NAME]', person_name)

        # Skicka e-postmeddelandet
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=settings.my_email, password=settings.password)
            connection.sendmail(
                from_addr=settings.my_email, 
                to_addrs=person_email,  # Skickar till varje persons e-post
                msg=f"Subject: Happy Birthday!!\n\n{personalized_letter}"
            )
else:
    print("Ingen har födelsedag idag.")

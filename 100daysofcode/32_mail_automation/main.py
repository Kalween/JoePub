import smtplib
import settings


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=settings.my_email, password=settings.password)
connection.sendmail(from_addr=settings.my_email, to_addrs="jrokcode@gmail.com", msg="hello")
connection.close()
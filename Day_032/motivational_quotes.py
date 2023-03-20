import datetime as dt
import smtplib
import random

my_email = "namlahco5@gmail.com"
my_password = "gcngjdcnwohhdjua"

today = dt.datetime.now()
day_of_week = today.weekday()


if day_of_week == 0:
    with open("Day_032/quotes.txt") as data:
        quotes = data.read().splitlines()
        random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sohier.lotfy@hotmail.com", msg=f"Subject:Today's quote\n\nToday's quote:\n{random_quote}")

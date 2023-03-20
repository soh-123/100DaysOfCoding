import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today_day = now.day
today_month = now.month

my_email = "namlahco5@gmail.com"
my_password = "gcngjdcnwohhdjua"

data = pandas.read_csv("Day_032/birthdays.csv")
bday_dict = data.to_dict(orient="records")

#--------------------------- Update Birthday File --------------------------------#

name = input("Please Enter Name: ")
email = input("Please Enter Email: ")
year_of_birth = input("Please Enter Birthdate:\nYear: ")
month = input("Month: ")
day = input("Day: ")

data_dict = {
    "name":[name],
    "email":[email],
    "year":[year_of_birth],
    "month":[month],
    "day":[day]
            }

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Day_032/birthdays.csv", mode="a", index=False, header=False)

#--------------------------- Check Today's date --------------------------------#

for bday in bday_dict:
    if bday["day"] == today_day and bday["month"] == today_month:
        print(today_month, today_day)
        reciever_name = bday["name"]
        reciever_email = bday["email"]

        with open(f"Day_032/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter_content = letter.read()

            new_letter = letter_content.replace("[NAME]", reciever_name).replace("Angela", "Sohier")

        with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=reciever_email, msg=f"Subject:Happy birthday {reciever_name}\n\n{new_letter}")
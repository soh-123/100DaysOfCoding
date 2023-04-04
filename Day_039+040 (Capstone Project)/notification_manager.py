from twilio.rest import Client
import os
import smtplib

TWILIO_SID = "AC31231ec2bafa0063a47a69117eaaef60"
AUTH_TOKEN = os.environ["AUTH_TOKEN"]

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
        
    def send_message(self, message):
        self.client = Client(TWILIO_SID, AUTH_TOKEN)
        sms_message = self.client.messages.create(
        body=message,
        from_="+14346029262",
        to="+971526738751"
        )
        print(sms_message.sid)

    
    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'))



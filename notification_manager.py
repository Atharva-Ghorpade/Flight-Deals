import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d0684b984e180ac45b31e794ec16b26b/flightDeals/users"


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.header = {
            'Authorization': 'Basic QXRoYXJ2YTE3MTA6QUA0MjEwOTc3'
        }

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_mails(self, msg_content):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.header)
        users_data = response.json()['users']
        login = os.environ["EMAIL"]
        password = os.environ["EMAIL_PASSWORD"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(login, password)
            for users in users_data:
                email = users['whatIsYourEmailAddress?']
                msg = MIMEMultipart()
                msg['From'] = login
                msg['To'] = email
                msg['Subject'] = 'Low Price Alert!'
                msg.attach(MIMEText(msg_content, 'plain'))
                try:
                    connection.send_message(msg=msg)
                    print(f"Email sent to {email} address!")

                except smtplib.SMTPRecipientsRefused:
                    print(f"Email {email} is invalid!")

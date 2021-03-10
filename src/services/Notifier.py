import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notifier:
    # Hardcoded email address to test notifier
    subscribers = {
        'Johannes': 'schmid.johannes90@gmail.com',
        'hannesxo': 'hannes322@yahoo.de'
    }
    # Creating messages container

    sender_email = 'festify.alerts@gmail.com'

    server = None

    def __init__(self):
        # Starting up server and establish connection
        sender_password = os.getenv('SENDERPASSWORD')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, sender_password)

    def notify(self, event):
        # creating e-mail message
        e_mail = MIMEMultipart('alternative')
        e_mail['From'] = self.sender_email
        e_mail['Subject'] = 'Festival News!'
        text = 'Hi!Some news! An event you have subscribed for has changed!'
        html = """<html>
            <head>
                <style>
                    body {background-color: #E7F3FF; color: #1c1e21;}
                </style>
            <body>
                    <p>Hi!<br>
                       Some news!<br>
                       An event you have subscribed for has changed!
                    </p>
            </body>
                """
        # Convert the multiline string into MIMETYPE HTML
        plain = MIMEText(text, 'plain')
        html = MIMEText(html, 'html')
        e_mail.attach(plain)
        e_mail.attach(html)


        for subscriber, address in self.subscribers.items():
            e_mail['To'] = address
            self.server.send_message(e_mail)

    def sendSummary(self, email):
        e_mail = MIMEMultipart('alternative')
        e_mail['To'] = email
        e_mail['From'] = self.sender_email
        e_mail['Subject'] = 'Here is your Summary'

        # Reading content from csv file
        df = pd.read_csv('data/changes.csv')
        df = df.sort_values(by=['last change'])
        htmlTable = df.to_html()
        text = df.to_string()

        # Convert the multiline string into MIMETYPE HTML
        plain = MIMEText(text, 'plain')
        html = MIMEText(htmlTable, 'html')
        e_mail.attach(plain)
        e_mail.attach(html)
        self.server.send_message(e_mail)


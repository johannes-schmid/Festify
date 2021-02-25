import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notifier:
    # Hardcoded email address to test notifier
    subscribers = {
        'Johannes': 'schmid.johannes90@gmail.com',
        'hannesxo': 'hannes322@yahoo.de'
    }
    # Creating messages container
    e_mail = MIMEMultipart('alternative')
    sender_email = 'festify.alerts@gmail.com'
    e_mail['From'] = sender_email
    server = None

    def __init__(self):
        # Starting up server and establish connection
        sender_password = os.getenv('SENDERPASSWORD')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, sender_password)

    def notify(self, event):
        # creating e-mail message
        self.e_mail['Subject'] = 'Festival News!'
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
        self.e_mail.attach(plain)
        self.e_mail.attach(html)


        for subscriber in self.subscribers:
            self.e_mail['To'] = self.subscribers[subscriber]
            self.server.send_message(self.e_mail)



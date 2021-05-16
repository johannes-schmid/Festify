import os
import smtplib
import pprint

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.services.Crawler import Crawler
from src.services.SubscriptionManager import SubscriptionManager



class Notifier:
    sender_email = 'festify.alerts@gmail.com'

    server = None

    def __init__(self):
        sender_password = os.getenv('SENDERPASSWORD')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, sender_password)
    # Starting up server and establish connection

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


        subMan = SubscriptionManager()
        subscribers = subMan.getSubscribers()

        for subscriber in subscribers:
            if 'email' in subscriber:
                del e_mail['To']
                e_mail['To'] = subscriber['email']
                self.server.send_message(e_mail)

    def sendSummary(self, email):
        e_mail = MIMEMultipart('alternative')
        e_mail['To'] = email
        e_mail['From'] = self.sender_email
        e_mail['Subject'] = 'Here is your Summary'

        # Reading content from csv file
        crawler = Crawler()
        events = crawler.getEvents()
        htmlContent = pprint.pformat(events)

        # Convert the multiline string into MIMETYPE HTML
        plain = MIMEText(htmlContent, 'plain')
        html = MIMEText(htmlContent, 'html')
        e_mail.attach(plain)
        e_mail.attach(html)
        self.server.send_message(e_mail)
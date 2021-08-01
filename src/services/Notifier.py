import os
import flask
from flask import render_template
from flask_mail import Mail, Message
from .SubscriptionManager import SubscriptionManager


class Notifier:
    sender_email = 'festify.alerts@gmail.com'
    server = None

    def __init__(self):
        flask.current_app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        flask.current_app.config['MAIL_PORT'] = 465
        flask.current_app.config['MAIL_USERNAME'] = 'festify.alerts@gmail.com'
        flask.current_app.config['MAIL_PASSWORD'] = os.getenv('SENDERPASSWORD')
        flask.current_app.config['MAIL_USE_TLS'] = False
        flask.current_app.config['MAIL_USE_SSL'] = True
        self.mail = Mail(flask.current_app)

    # Starting up server and establish connection

    def notify(self, event):
        # creating e-mail message
        subMan = SubscriptionManager()
        subscribers = subMan.getSubscribers()
        for subscriber in subscribers:
            if 'email' in subscriber:
                msg = Message('Festival News', sender='festify.alerts@gmail.com', recipients=[subscriber['email']])
                msg.html = render_template('mail.html', event=event)
                self.mail.send(msg)

    def sendSummary(self, email, events):
        msg = Message('Festival Summery', sender='festify.alerts@gmail.com', recipients=[email])
        msg.html = render_template('summarymail.html', events=events)
        self.mail.send(msg)

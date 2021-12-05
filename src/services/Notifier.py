import os
import flask
from flask import render_template
from flask_mail import Message
from .SubscriptionManager import SubscriptionManager
# Import the Secret Manager client library.
from google.cloud import secretmanager
import sendgrid
from sendgrid.helpers.mail import *

class Notifier:
    sender_email = 'festify.alerts@gmail.com'
    server = None

    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(api_key="")

        # flask.current_app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        # flask.current_app.config['MAIL_PORT'] = 465
        # flask.current_app.config['MAIL_USERNAME'] = 'festify.alerts@gmail.com'
        # flask.current_app.config['MAIL_PASSWORD'] = self.getGmailPassword()
        # flask.current_app.config['MAIL_USE_TLS'] = False
        # flask.current_app.config['MAIL_USE_SSL'] = True
        # self.mail = Mail(flask.current_app)

    # Starting up server and establish connection

    def notify(self, event):
        # creating e-mail message

        subMan = SubscriptionManager()
        subscribers = subMan.getSubscribers()
        for subscriber in subscribers:
            if 'email' in subscriber:

                from_email = Email("festify.alerts@gmail.com")
                to_email = To(subscriber['email'])
                subject = event['name']
                content = Content("text/html", render_template('mail.html', event=event))
                mail = Mail(from_email, to_email, subject, content)
                try:
                    response = self.sg.client.mail.send.post(request_body=mail.get())
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
                except Exception as e:
                    print(e)

                # msg = Message('Festival News', sender='festify.alerts@gmail.com', recipients=[subscriber['email']])
                # msg.html =
                # self.mail.send(msg)

    def sendSummary(self, email, events):
        msg = Message('Festival Summery', sender='festify.alerts@gmail.com', recipients=[email])
        msg.html = render_template('summarymail.html', events=events)
        self.mail.send(msg)

    def getGmailPassword(self):

        # GCP project in which to store secrets in Secret Manager.
        project_id = "festify-321320"

        # ID of the secret to create.
        secret_id = "GMAIL_PASSWORD"

        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        # Add the secret version.
        version = 1

        # Access the secret version.

        secret_path = client.secret_version_path(project_id, secret_id, version)
        response = client.access_secret_version(request={"name": secret_path})
        return response.payload.data.decode('UTF-8')
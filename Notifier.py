import os
import smtplib




class Notifier:
    # Hardcoded email address to test notifier
    subscribers = {
        'Johannes': 'schmid.johannes90@gmail.com',
        'hannesxo': 'hannes322@yahoo.de'
    }

    sender_email = 'festify.alerts@gmail.com'
    server = None

    def __init__(self):
        sender_password = os.getenv('SENDERPASSWORD')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, sender_password)

    def notify(self, event):
        e_mail_message = f'Subject: Festival News!\n \nThere is a new change for the Event {event}, check of the website for tickets!'
        for subscriber in self.subscribers:
            receiver_mail = self.subscribers[subscriber]
            self.server.sendmail(self.sender_email, receiver_mail, e_mail_message)



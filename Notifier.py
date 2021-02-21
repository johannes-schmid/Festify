import os
import smtplib




class Notifier:
    # Hardcoded email address to test notifier
    subscribers = {
        'Johannes': 'schmid.johannes90@gmail.com',
        'hannesxo': 'hannes322@yahoo.de'

    }

    def notify(self, msg):
        for subscriber in self.subscribers:
            sender_email = 'festify.alerts@gmail.com'
            sender_password = os.environ.get('senderpassword')
            receiver_mail = self.subscribers[subscriber]
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_mail, msg)



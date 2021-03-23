from flask import Flask, render_template
from src.services.SubscriptionManager import SubscriptionManager
app = Flask(__name__)

changed_events = [
    {
        'Name': 'Dekmantel',
        'Date': '25-04-2021',
        'Website': 'www.dekmantel.com'
    },
    {
        'Name': 'Event2',
        'Date': '25-04-2021',
        'Website': 'www.event2.com'
    }
]

test = SubscriptionManager()
test.subscribe('Hubi','Hansi','hansi@hansi.de')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mail')
def mail():
    return render_template("mail.html", events=changed_events)


if __name__ == '__main__':
    app.run()



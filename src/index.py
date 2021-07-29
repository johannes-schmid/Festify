from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from src.services.Crawler import Crawler
from src.services.Notifier import Notifier
from src.services.SubscriptionManager import SubscriptionManager

app = Flask(__name__)

@app.route('/')
def index():
    crawler = Crawler()
    events = crawler.getEvents()
    return render_template("index.html", events = events)

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    subscriptionManager = SubscriptionManager()
    try:
        subscriptionManager.subscribe(firstname,lastname,email)
        return render_template("success.html", email=email)
    except:
        return redirect(url_for('failed'))

@app.route('/failed')
def failed():
    return render_template("failed.html")


@app.route('/summarymail')
def mail():
    crawler = Crawler()
    events = crawler.getEvents()
    notifier = Notifier()
    notifier.sendSummary("hannes322@yahoo.de", events)
    return "Email send hihi"

@app.route('/runcrawler')
def crawler():
    crawler = Crawler()
    crawler.run()
    return "Email send hihi"


if __name__ == '__main__':
    app.run()



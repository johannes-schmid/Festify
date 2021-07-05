from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from src.services.Crawler import Crawler
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


@app.route('/mail')
def mail():
    return render_template("mail.html")


if __name__ == '__main__':
    app.run()



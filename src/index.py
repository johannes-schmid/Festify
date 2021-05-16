from flask import Flask, render_template
from src.services.SubscriptionManager import SubscriptionManager
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/subscribe')
def index():
    return render_template("subscribe.html")

@app.route('/success')
def index():
    return render_template("success.html")

@app.route('/failed')
def index():
    return render_template("failed.html")

# @app.route('/mail')
# def mail():
#     return render_template("mail.html", events=changed_events)


if __name__ == '__main__':
    app.run()



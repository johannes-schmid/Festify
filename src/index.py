from flask import Flask, render_template

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




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mail')
def mail():
    return render_template("mail.html", events=changed_events)


if __name__ == '__main__':
    app.run()



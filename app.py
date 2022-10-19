from flask import Flask, render_template, session, redirect, url_for, request
from flask_mail import Mail, Message
import os

app = Flask('app')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hutimk@gmail.com'
app.config['MAIL_PASSWORD'] = 'qaimihqwugcdznfo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def sendEmail(result):
    msg = Message("Contact Form from Website", sender="hutimk@gmail.com", recipients=["hutimk@gmail.com"])

    msg.body = """
    Hello there,
    You just received a contact form.
    Name: {}
    Email: {}
    Message: {}
    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)


@app.route('/')
def index():
    return render_template("/index.html", current="home")

@app.route("/programs")
def programs():
    return render_template("/programs.html", current="programs")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/branches")
def branches():
    return render_template("branches.html", current="branches")

@app.route("/resources")
def resources():
    return render_template("resources.html", current="resources")

@app.route("/sendMail", methods=['GET', 'POST'])
def sendMail():
    result = {}
    result['name'] = request.form['name']
    result['email'] = request.form['email'].replace(' ', '').lower()
    result['message'] = request.form['message']
    sendEmail(result)
    return redirect("/contact")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)
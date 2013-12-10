#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import json

app = Flask(__name__)

@app.route('/api/contact', methods=['POST'])
def send_mail():
    msg = MIMEMultipart()
    fromaddr = 'bot@maestr0.com'
    toaddr = 'uliana@uliana.me'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Contact from website: {name}, <{email}>".format(
        name=request.form['name'],
        email=request.form['email']
    )
    body = request.form['text']
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("bot@caceres.me", "Lar1saGl0b@")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        resp = {"msg": "Message sent"}
        return json.dumps(resp)
    except Exception as ex:
        resp = {"msg": "Currently message cannot be sent, sorry for that",
                "error": str(ex)}
        return json.dumps(resp), 400


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

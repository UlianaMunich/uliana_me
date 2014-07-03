from django.shortcuts import render_to_response
from django.http import HttpResponse
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import json

def index(request):
     return render_to_response('index.html')

def send_mail(request):
    if request.method == 'POST':
        msg = MIMEMultipart()
        fromaddr = 'bot@maestr0.com'
        toaddr = 'uliana@uliana.me'
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Contact from website: {name}, <{email}>".format(
            name=request.POST['name'],
            email=request.POST['email']
        )
        body = request.POST['text']
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
            return HttpResponse(json.dumps(resp))
        except Exception as ex:
            resp = {"msg": "Currently message cannot be sent, sorry for that",
                    "error": str(ex)}
            return HttpResponse(json.dumps(resp), status=400)

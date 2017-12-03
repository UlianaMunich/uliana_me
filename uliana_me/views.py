from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json


def home(request):
    conferences = settings.CONFERENCES[:]
    for talk in conferences:
        talk['meta'] = {
            'thumbnail': "images/portfolio/%s_thumb.jpg" % talk['slug'],
            'preview_type': "youtube" if talk.get('youtube_id') else "image"
        }
        if talk['meta']['preview_type'] == 'youtube':
            talk['meta']['preview'] = 'https://www.youtube.com/embed/%s' % talk['youtube_id']
        elif talk['meta']['preview_type'] == 'image':
            talk['meta']['preview'] = "images/portfolio/%s.jpg" % talk['slug']
    context = {
        'conferences': conferences,
    }
    return render(request, 'index.html', context)

def career(request):
    return render_to_response('career.html')

def education(request):
    return render_to_response('education.html')

def certificates(request):
    return render_to_response('certificates.html')

def hobby(request):
    return render_to_response('hobby.html')

def contact(request):
    return render(request, 'contact.html')

# API
def send_mail(request):
    if request.method == 'POST':
        msg = MIMEMultipart()
        fromaddr = settings.EMAIL_FROM
        emailpass = settings.EMAIL_PASS
        toaddr = settings.ADMINS[0][1]
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
            server.login(fromaddr, emailpass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            resp = {"msg": "Message sent"}
            return HttpResponse(json.dumps(resp))
        except Exception as ex:
            resp = {"msg": "Currently the message cannot be sent, sorry for that",
                    "error": str(ex)}
            return HttpResponse(json.dumps(resp), status=400)

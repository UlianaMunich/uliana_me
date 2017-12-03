# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from uliana_me import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^career?/$', views.career),
    url(r'^education?/$', views.education),
    url(r'^certificates?/$', views.certificates),
    url(r'^hobby?/$', views.hobby),
    url(r'^contact?/$', views.contact),
    url(r'^api/contact$', views.send_mail),
    url(r'^linkedin/?$', RedirectView.as_view(
        url='https://www.linkedin.com/in/ulianaa/')),
    url(r'^twitter/?$', RedirectView.as_view(
        url='https://twitter.com/ui_me1')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

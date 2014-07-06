from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index'),
    url(r'^career?/$', 'views.career'),
    url(r'^education?/$', 'views.education'),
    url(r'^certificates?/$', 'views.certificates'),
    url(r'^hobby?/$', 'views.hobby'),
    url(r'^contact?/$', 'views.contact'),
    url(r'^api/contact$', 'views.send_mail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),
    )
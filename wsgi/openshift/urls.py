from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.index'),
    url(r'^career?/$', 'views.career'),
    url(r'^education?/$', 'views.education'),
    url(r'^certificates?/$', 'views.certificates'),
    url(r'^hobby?/$', 'views.hobby'),
    url(r'^contact?/$', 'views.contact'),
    url(r'^api/contact$', 'views.send_mail'),
    url(r'^admin/', include(admin.site.urls)),
)
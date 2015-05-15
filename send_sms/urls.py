#django
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name='Login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='Logout'),
    url(r'^send-sms/$', 'send_sms.views.sendSMS', name='Send SMS'),
    url(r'^messages/(?P<page>[0-9]{1})$', 'send_sms.views.getMessages', name='Messages'),
    url(r'^contacts/(?P<page>[0-9]{1})$', 'send_sms.views.viewContact', name='Contacts'),
    url(r'^contacts/edit/(?P<num>[0-9]+)$', 'send_sms.views.editContact', name='EditContact'),
    url(r'^contacts/delete/(?P<num>[0-9]+)$', 'send_sms.views.deleteContact', name='DeleteContact'),
    # url(r'^analytics/$', 'send_sms.views.viewAnalytics', name='Analytics'), TODO
    url(r'^template/$', 'send_sms.views.createTemplate', name='CreateTemplate'),
)

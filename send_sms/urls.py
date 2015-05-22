#django
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name='Login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='Logout'),
    url(r'^send-sms/$', 'send_sms.views.sendSMS', name='Send SMS'),
    url(r'^messages/(?P<page>[0-9]+)$', 'send_sms.views.getMessages', name='Messages'),
    url(r'^contacts/(?P<page>[0-9]+)$', 'send_sms.views.viewContact', name='Contacts'),
    url(r'^contacts/edit/(?P<num>[0-9]+)$', 'send_sms.views.editContact', name='EditContact'),
    url(r'^contacts/edit-group/(?P<groupID>[0-9]+)$', 'send_sms.views.editGroup', name='EditGroup'),
    url(r'^contacts/delete/(?P<num>[0-9]+)$', 'send_sms.views.deleteContact', name='DeleteContact'),
    url(r'^template/$', 'send_sms.views.createTemplate', name='CreateTemplate'),
    url(r'^template/(?P<templateID>[0-9]+)$', 'send_sms.views.editTemplate', name='EditTemplate'),
    url(r'^template/delete/(?P<templateID>[0-9]+)$', 'send_sms.views.deleteTemplate', name='DeleteTemplate'),

    # url(r'^sandbox/$',  'send_sms.views.sandbox', name='Login'),
)

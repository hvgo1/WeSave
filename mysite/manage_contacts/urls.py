from django.conf.urls import patterns, url

from manage_contacts import views

urlpatterns = patterns('',
    url(r'^$', views.contactUs, name='contactus'),
)

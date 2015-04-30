from django.conf.urls import patterns, url

from verify_campaign import views

urlpatterns = patterns('',
    url(r'^$', views.verify, name="verify"),
)
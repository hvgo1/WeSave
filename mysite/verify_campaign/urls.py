from django.conf.urls import patterns, url

from verify_campaign import views

urlpatterns = patterns('',
    url(r'^$', views.forapproval_campaigns, name="forapproval_campaigns"),
    url(r'all', views.approve, name="approve"),
)
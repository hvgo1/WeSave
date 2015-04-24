from django.conf.urls import patterns, url

from maintain_profile import views

urlpatterns = patterns('',
    url(r'^list', views.listProfile, name='listprofile'),
    #url(r'^(?P<username>\w+)', views.viewProfile, name='viewprofile'),
    url(r'^campaign', views.campaign, name='campaign')
)

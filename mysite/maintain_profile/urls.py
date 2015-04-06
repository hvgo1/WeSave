from django.conf.urls import patterns, url

from maintain_profile import views

urlpatterns = patterns('',
    #url(r'^list', views.profileList, name='pelistrofil'),
    url(r'^(?P<username>\w+)', views.viewProfile, name='viewprofile')
)

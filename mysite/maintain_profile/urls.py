from django.conf.urls import patterns, url

from maintain_profile import views

urlpatterns = patterns('',
    url(r'^list', views.listProfile, name='listprofile'),
    url(r'^update/(?P<username>\w+)', views.updateProfile, name='updateprofile'),
    url(r'^(?P<username>\w+)', views.viewProfile, name='viewprofile'),

)

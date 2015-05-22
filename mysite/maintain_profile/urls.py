from django.conf.urls import patterns, url

from maintain_profile import views

urlpatterns = patterns('',
    url(r'^list', views.list_profile, name='listprofile'),
    url(r'^update/(?P<username>\w+)', views.update_profile, name='updateprofile'),
    url(r'^(?P<username>\w+)', views.view_profile, name='viewprofile'),

)

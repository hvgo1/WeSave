from django.conf.urls import patterns, url
from  reallocate_donation import views

urlpatterns = patterns('',
    url(r'^$', views.reallocate, name='reallocate'),
)

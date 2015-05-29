from django.conf.urls import patterns, url

from donate import views

urlpatterns = patterns('',
    url(r'^in-kind/(?P<campaign_title_slug>[\w\-]+)/$', views.donate_inkind, name='donateinkind'),
    url(r'^monetary/(?P<campaign_title_slug>[\w\-]+)/$', views.donate_monetary, name='donatemonetary'),
    #url(r'^common/fund', views.update_profile, name='updateprofile'),
    #url(r'^common/goods', views.view_profile, name='viewprofile'),

)

from django.conf.urls import patterns, url

from donate import views

urlpatterns = patterns('',
    url(r'^in-kind/(?P<campaign_title_slug>[\w\-]+)/$', views.donateInkind, name='donateinkind'),
    url(r'^monetary/(?P<campaign_title_slug>[\w\-]+)/$', views.donateMonetary, name='donatemonetary'),
    url(r'^monetary/(?P<campaign_title_slug>[\w\-]+)/cancelled/$', views.cancelled, name='cancelled'),
    url(r'^monetary/(?P<campaign_title_slug>[\w\-]+)/success/$', views.success, name='success'),
    #url(r'^common/fund', views.update_profile, name='updateprofile'),
    #url(r'^common/goods', views.view_profile, name='viewprofile'),

)

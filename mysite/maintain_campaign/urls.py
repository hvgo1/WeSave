from django.conf.urls import patterns, url
from maintain_campaign import views

urlpatterns = patterns('', 
    #url(r'^$', views.index, name='index'),
    url(r'^add/(?P<username>\w+)/$', views.addCampaign, name='add_campaign'),
    url(r'^view/(?P<campaign_title_slug>[\w\-]+)/$', views.viewCampaign, name='view_campaign'),
    url(r'^update/(?P<id>\d+)/$', views.updateCampaign, name='update_campaign'),
    url(r'^list/$', views.listCampaign, name='list_campaign'),
    )

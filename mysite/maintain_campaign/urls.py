from django.conf.urls import patterns, url
from maintain_campaign import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^add/(?P<username>\w+)', views.addCampaign, name='add_campaign'),
    url(r'^(?P<campaign_title_slug>[\w\-]+)/$', views.viewCampaign, name='view_campaign'),
    )

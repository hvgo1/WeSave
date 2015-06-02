
from django.conf.urls import patterns, url, include
from maintain_campaign import views
import donate
import reallocate_donation 

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^add/(?P<username>\w+)/$', views.addCampaign, name='add_campaign'),
    url(r'^view/(?P<campaign_title_slug>[\w\-]+)/$', views.viewCampaign, name='view_campaign'),
    url(r'^update/(?P<id>\d+)/$', views.updateCampaign, name='update_campaign'),
    url(r'^list/$', views.listCampaign, name='list_campaign'),
    url(r'^view-details/reallocate/(?P<id>\d+)/$', include('reallocate_donation.urls'), name='reallocate'),
    url(r'^view-details/$', views.viewCampaignDetails, name='view_campaign_details'),
    url(r'^donate/', include('donate.urls', namespace="donate")),
    )

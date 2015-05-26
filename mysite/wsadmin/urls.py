from django.conf.urls import patterns, url, include
import verify_campaign
from wsadmin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^approve/', include('verify_campaign.urls',namespace="approve")),
    url(r'^manage-social-workers/', include('manage_social_workers.urls',namespace="manage_social_workers")),
    url(r'^campaign/', include('maintain_campaign.urls', namespace="list_campaign_details")),
)

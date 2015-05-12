from django.conf.urls import patterns, url, include
import verify_campaign
from wsadmin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^approve/', include('verify_campaign.urls',namespace="approve")),
)

from django.conf.urls import patterns, url
from maintain_campaign import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^add/(?P<username>\w+)', views.add_campaign, name='add_campaign'),
    url(r'^view/$', views.view_campaign, name='view_campaign'),
    )

from django.conf.urls import patterns, url
from maintain_campaign import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^add_campaign/(?P<username>\w+)', views.add_campaign, name='add_campaign'),
    )

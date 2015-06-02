from django.conf.urls import patterns, url

from manage_social_workers import views

urlpatterns = patterns('',
    url(r'^$', views.usersList, name='userslist'),
    url(r'add-role', views.addRole, name="add_role"),

)


from django.conf.urls import patterns, url

from manage_social_workers import views

urlpatterns = patterns('',
    url(r'^$', views.users_list, name='userslist'),
    url(r'add-role', views.add_role, name="add_role"),

)


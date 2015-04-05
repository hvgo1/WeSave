from registration.backends.simple.views import RegistrationView #
from mysite import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        if 'indivbutton' in request.POST:
            return '/reg-individual/%s'  %user.username #SECURITY ISSUE(?)
        else:
            return '/reg-group/%s' %user.username

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^reg-individual/(?P<username>\w+)', views.register_individual, name='register_individual'),
    url(r'^reg-group/(?P<username>\w+)', views.register_group, name='register_group'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

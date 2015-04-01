from registration.backends.simple.views import RegistrationView #
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/home/'

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'mysite.views.home', name='home'),
    #url(r'^register/', 'mysite.views.register', name='register'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

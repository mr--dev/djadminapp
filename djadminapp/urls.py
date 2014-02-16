from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djadminapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('appmanager.urls')),
    url(r'^appmanager/', include('appmanager.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

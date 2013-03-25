from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.sites.models import Site
admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^tasting_app/', include('tasting_app.foo.urls')),

    url(r'^$', 'misc.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

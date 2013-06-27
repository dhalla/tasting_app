from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns(

    '',

    # Home / Home Redirect
    #url(r'^$', RedirectView.as_view(url='/misc/home')),
    url(r'^$', 'misc.views.home', name='home'),

    # Misc
    url(r'^misc/', include('misc.urls')),

    # Bar
    url(r'^bar/', include('bar.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

)

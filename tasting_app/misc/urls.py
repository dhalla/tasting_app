# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

urlpatterns = patterns(

    'misc.views',

    # Home
    url(r'^home/$', 'home', name='home'),

)

# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

urlpatterns = patterns(

    'bar.views',

    # Home
    url(r'^list/$', 'list', name='bar_list'),

)

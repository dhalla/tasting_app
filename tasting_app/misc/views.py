# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import *
from django.core.urlresolvers import reverse, resolve
from django.core import serializers
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib import messages

from bar.models import *

def home(request):
    """ Display Homepage """

    scotch_list = Spirit.objects.all()

    return render_to_response(
        'misc/home.html',
        {
            'scotch_list': scotch_list,
        },
        context_instance=RequestContext(request)
    )

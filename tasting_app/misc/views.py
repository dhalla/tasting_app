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
    user_str = str(request.user)

    return render_to_response(
        'home.html',
        {
            'scotch_list': scotch_list,
            'user': user_str
        },
        context_instance=RequestContext(request)
    )

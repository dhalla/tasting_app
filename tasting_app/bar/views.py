# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import *
from django.core.urlresolvers import reverse, resolve
from django.core import serializers
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.contrib import messages

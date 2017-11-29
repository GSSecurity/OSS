# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    context = {}
    template = loader.get_template('../templates/index.html')

    return HttpResponse(template.render(context, request))
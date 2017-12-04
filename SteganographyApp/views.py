# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
# Create your views here.
from django.template import loader


def index(request):
    context = {}
    template = loader.get_template('../templates/index.html')

    return HttpResponse(template.render(context, request))

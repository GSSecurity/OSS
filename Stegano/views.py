# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader

from Stegano.forms import UploadFileForm
from Stegano.models import SaveInfo

from steganography.steganography import Steganography
from django.utils.encoding import smart_str
import os


def index(request):
    context = {}
    template = loader.get_template('../templates/index.html')

    # Upload Handler
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # form.user_ip = request.META['REMOTE_ADDR']
        # form.user_agent = request.META['HTTP_USER_AGENT']
        # form.save()
        if form.is_valid():
            files = form.save()
            print("UPLOADED : ", files.input_img.path) # file path
            print("KEY : ", form.data['input_key']) # encryption key
            print("MSG : ", form.data['input_msg']) # plain text

            inputpath = files.input_img.path
            filename = inputpath.split("/")[-1]
            text = form.data['input_msg']
            outputpath = ("/".join(inputpath.split("/")[0:-2])) + "/static/img/" + filename
            
            try :
                Steganography.encode(inputpath, outputpath, text)
                print ("SAVED : ", outputpath)
            except:
                print "Encode Error"
                return HttpResponseRedirect('/')

            try:
                outputfile = open(outputpath, "r")
                form.success = True
                form.save()
            except:
                print "File Open Error"
                return HttpResponseRedirect('/')
            
            try:
                response = HttpResponse(outputfile.read())
                response['Content_type']= 'application/force-download'
                response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
                response['Content-Length'] = os.path.getsize(outputpath)
                return response
            except:
                print "HttpResponse Error"
                return HttpResponseRedirect('/')    
        else:
            print(form.errors)
            print(form.error_class)
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
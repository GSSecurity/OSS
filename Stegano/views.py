# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import sys

sys.path.append('../lib/steganography/steganography')

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader

from Stegano.forms import *
from Stegano.models import SaveInfo
from lib.steganography.steganography import Steganography, keyInput
from django.utils.encoding import smart_str
import os


def index(request):
    context = {}
    template = loader.get_template('../templates/index.html')

    # Upload Handler
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) if int(request.POST['mode']) else ExtractFileForm(
            request.POST, request.FILES)

        # form.user_ip = request.META['REMOTE_ADDR']
        # form.user_agent = request.META['HTTP_USER_AGENT']
        # form.save()
        if form.is_valid():
            files = form.save()
            if (int(form.data['mode'])):
                print("UPLOADED : ", files.input_img.path)  # file path
                print("KEY : ", form.data['input_key'])  # encryption key
                print("MSG : ", form.data['input_msg'])  # plain text
                # print("MODE : ", form.data['mode']) # processing mode
                # print("type : ", type(str(form.data['mode'])))
                inputpath = files.input_img.path
                filename = inputpath.split("/")[-1]
                text = form.data['input_msg']
                outputpath = ("/".join(inputpath.split("/")[0:-2])) + "/static/img/" + filename

                try:
                    Steganography.encode(inputpath, outputpath, keyInput(form.data['input_key']) + text)
                    print ("SAVED : ", outputpath)
                except:
                    print "Encode Error"
                    return HttpResponseRedirect('/')

                try:
                    # noinspection PyTypeChecker
                    outputfile = open(outputpath, "r")
                    form.success = True
                    form.save()
                except:
                    print "File Open Error"
                    return HttpResponseRedirect('/')

                try:
                    response = HttpResponse(outputfile.read())
                    response['Content_type'] = 'application/force-download'
                    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
                    response['X-Sendfile'] = smart_str(filename)
                    response['Content-Length'] = os.path.getsize(outputpath)
                    return response
                except:
                    print "HttpResponse Error"
                    return HttpResponseRedirect('/')
            else:
                print("UPLOADED : ", files.input_img.path)
                print("KEY : ", form.data['input_key'])
                inputpath = files.input_img.path
                filename = inputpath.split("/")[-1].split(".")[0] + ".txt"
                try:
                    secretCode = keyInput(form.data['input_key'])
                    secretCodeLength = len(secretCode)

                    text = Steganography.decode(inputpath)

                    # check Secret Key
                    leakSecretCode = text[0:secretCodeLength]
                    if secretCode == leakSecretCode:
                        print("Your secret message was \"%s\"" % text[secretCodeLength:])
                        return HttpResponseRedirect('/?flavour=%s' % text[secretCodeLength:])
                    else:
                        print("You are not permited!!")
                        return HttpResponseRedirect('/?flavour=#')
                    print ("text : " + text)
                except:
                    print("Not Encoding file")
                    return HttpResponse("/")

                    # try:
                    #     # response = HttpResponse(text)
                    #     # response['Content_type']= 'application/force-download'
                    #     # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
                    #     # response['Content-Length'] = len(filename)
                    #     # return response
                    #
                    # except:
                    #     print "HttpResponse Error"
                    #     return HttpResponseRedirect('/')
        else:
            print(form.errors)
            print(form.error_class)
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


'''
def read_text(request):
    if request.method == 'POST':
        form = ExtractFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("INPUT KEY : ", form.data['input_key'])
            #print("ORIGINAL KEY : ", form.object.raw(""))
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            print(form.error_class)
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
        '''

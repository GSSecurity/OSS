# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader

from Stegano.forms import UploadFileForm
from Stegano.models import SaveInfo

from steganography.steganography import Steganography


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


            # 1. 위 3개 인자로 스테가노그래피 처리를 해서
            # 2. output파일을 static/img 폴더에 저장하고
            # 3. URL 계산을 해서
            inputpath = files.input_img.path
            filename = inputpath.split("/")[-1]
            text = form.data['input_msg']
            outputpath = "/var/www/OSS/static/img/enc_" + filename #temp path (absolute)
            print ("SAVED : ", outputpath)
            try :
                Steganography.encode(inputpath, outputpath, text)
                # 성공하면 반환하기 전에 아래 두줄 실행
                # form.success = True
                # form.save()
                form.success = True
                form.save()
                return HttpResponseRedirect("/static/img/enc_" + filename)
            except :
                # 4. HttpResponseRedirect 경로를 3의 URL 주소로 던지면 됨
                print ("encode error")
                return HttpResponseRedirect('/')
            
        else:
            print(form.errors)
            print(form.error_class)
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
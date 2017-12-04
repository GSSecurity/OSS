# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.utils import timezone


class SaveInfo(models.Model):
    user_ip = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=1024)
    access_time = models.DateTimeField(default=timezone.now)
    input_msg = models.CharField(max_length=4400, default="")
    input_key = models.CharField(max_length=4400, default="GSSGSSGSSGSS")
    input_img = models.FileField(null=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return self.user_ip
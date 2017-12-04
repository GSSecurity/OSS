# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class SaveInfo(models.Model):
    user_ip = models.CharField(max_length=20)
    user_plain_text = models.CharField(max_length=4400)
    user_agent = models.CharField(max_length=1024)
    user_file = models.FileField()
    access_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_ip

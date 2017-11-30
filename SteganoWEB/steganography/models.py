# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Save_Info(models.Model):
	User_IP = models.CharField(max_length=20)
	User_Plain_Text = models.CharField(max_length=4400)
	User_Agent = models.CharFiled(max_length=1024)
	Access_Time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.User_IP
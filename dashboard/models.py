# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,)
    date_of_birth=models.DateField(blank=True,null=True)
    description=models.CharField(blank=False,null=False,max_length=50,default='not sure')
    profile_image=models.ImageField(upload_to='profilepic/',blank=True)
    about_me=models.TextField(max_length=150,blank=True)
    place=models.CharField(max_length=20,blank=True,null=True)


    def __str__(self):
        return self.user.username

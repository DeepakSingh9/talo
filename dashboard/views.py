# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Profile
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'dashboard/home.html',{})

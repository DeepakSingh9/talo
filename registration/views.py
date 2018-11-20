# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from forms  import LoginForm,RegistrationForm


# Create your views here.



def auth_login(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile',pk=user.pk)
        else:
            return HttpResponse('Please fill the  form')

    return render(request,'registration/login.html',{})



def registration(request):
    if request.method=='POST':
        regform=RegistrationForm(request.POST)
        userform=LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']

        if regform.is_valid() and userform.is_valid():
            user=userform.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=regform.save(request.POST)
            profile.user=user
            profile.save()

            return redirect('profile',pk=user.pk)
        else:
            return HttpResponse('Please fill the form correctly')
    else:
        regform=RegistrationForm()
        userform=LoginForm()
    return render(request,'registration/signup.html',{'regform':regform,'userform':userform})

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render,redirect
from .forms import *

def signup(request):
    form=CreateUserform()

    if request.method == 'POST':
        form=CreateUserform(request.POST)
        if form.is_valid():
            form.save()

    context={'form' : form}
    return render(request,'signup.html',context)

def login(request):
    context={}
    return render(request,'login.html',context)

def Sass(request):

    form=SassForm()
    
    if request.method == 'POST':
        form=SassForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render (request,'sass.html',context)

def Sonas(request):

    form=SonasForm()

    if request.method == 'POST':
        form=SonasForm(request.POST)
        if form.is_valid():
            form.save()
      
    context={'form':form}
    return render (request,'sonas.html',context)







class SassAPIView(generics.CreateAPIView):
  permission_classes=(AllowAny,)
  serializer_class=SassSerializer
  
class SassViewSet(viewsets.ModelViewSet):
    # define queryset
  queryset = SassProposal.objects.all()
 
    # specify serializer to be used
  serializer_class = SassSerializer

class SonasAPIView(generics.CreateAPIView):
  permission_classes=(AllowAny,)
  serializer_class=SonasSerializer

class SonasViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = SonasProposal.objects.all()
 
    # specify serializer to be used
    serializer_class = SonasSerializer

def SassCreate(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = SassForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "sass.html", context)
    
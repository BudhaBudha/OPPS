from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render
from django import forms

# Class based view to Get User Details using Token Authentication
class StudentDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = Student.objects.get(id=request.user.id)
    serializer = StudentSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class StudentRegisterAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = StudentRegisterSerializer

class LecturerDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = Lecturer.objects.get(id=request.user.id)
    serializer = LecturerSerializer(user)
    return Response(serializer.data)

class LecturerRegisterAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = LecturerRegisterSerializer

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
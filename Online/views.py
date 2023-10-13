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
from .models import *
from django.shortcuts import render,redirect
from django import forms

def signup(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        st = request.POST.get('student')
        te = request.POST.get('teacher')
        
        user = User.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()
        
        usert = None
        if st:
            usert = user_type(user=user,is_student=True)
        elif te:
            usert = user_type(user=user,is_teach=True)
        
        usert.save()
        #Successfully registered. Redirect to homepage
        return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('shome') #Go to student home
            elif user.is_authenticated and type_obj.is_teach:
                return redirect('thome') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('home')

    return render(request, 'login.html')

def Phome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request,'student_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return redirect('thome')
    else:
        return redirect('login')
                      
def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return render(request,'teacher_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('shome')
    else:
        return redirect('home')







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
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
        name = request.POST['name']
        problem = request.POST['problem']
        design = request.POST['design']
        gender = request.POST['gender']
        risks = request.POST['risks']
        evaluations = request.POST['evaluations']
        team = request.POST['team']
        purpose = request.POST['purpose']
        ethics = request.POST['ethics']
        proposal = SassProposal(proposal_name=name,
                                Project_design=design,
                                Research_purpose=purpose,
                                Problem_identification=problem,
                                Gender_equality=gender,
                                Research_ethics=ethics,
                                Critical_risks=risks,
                                Monitoring_Evaluation=evaluations,
                                Project_Team=team)
        proposal.save()
        # if form.is_valid():
        #     form.save()
            # return redirect("")
        # return redirect('/ ')
    # context={'form':form}
    return render (request,'sass.html')

def Sonas(request):

    form=SonasForm()

    if request.method == 'POST':
        name = request.POST['name']
        statement = request.POST['statement']
        proposal = request.POST['proposal']
        environment = request.POST['environment']
        team = request.POST['team']
        ethics = request.POST['ethics']
        funding = request.POST['funding']
        timeline = request.POST['timeline']
        budget = request.POST['funding']
        biosketch = request.FILES['file']
        sonas_proposal = SonasProposal(
            proposal_name = name,
            Personal_statement = statement,
            Research_environment = environment,
            Research_Team_Capacity = team,
            IRB_Ethics = ethics,
            Additional_funding = funding,
            Project_Timeline = timeline,
            Research_Proposal = proposal,
            Budget = budget,
            NHIF_Biosketch = biosketch
        )
        sonas_proposal.save()
    # context={'form':form}
    return render (request,'sonas.html')
  

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
    
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
#from django.contrib.auth import get_user_model


# Create your models here.

class SassProposal(models.Model):
    #proposer=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='reg_no')
    #lecturer=models.ForeignKey(Lecturer,on_delete=models.SET_NULL,null=True)
    proposal_name = models.SlugField(max_length=80, unique=True)
    Problem_identification=models.TextField(max_length=1000)
    Research_purpose=models.TextField(max_length=800)
    Project_design=models.TextField(max_length=1000)
    Gender_equality=models.TextField(max_length=500)
    Research_ethics=models.TextField(max_length=500)
    Critical_risks=models.TextField(max_length=500)
    Monitoring_Evaluation=models.TextField(max_length=700)
    Project_Team=models.TextField(max_length=500)
    def __str__(self):
        return self.proposal_name 

class SonasProposal(models.Model):
    #proposer=models.ForeignKey(Student,on_delete=models.CASCADE)
    #lecturer=models.ForeignKey(Lecturer,on_delete=models.SET_NULL,null=True)
    proposal_name = models.SlugField(max_length=80, unique=True)
    Personal_statement=models.TextField(max_length=799)
    Research_Proposal=models.TextField(max_length=999)
    Research_environment=models.TextField(max_length=500)
    Research_Team_Capacity=models.TextField(max_length=500)
    IRB_Ethics=models.TextField(max_length=299)
    Additional_funding=models.TextField(max_length=299)
    Project_Timeline=models.TextField(max_length=499)
    Budget=models.TextField(max_length=499)
    NHIF_Biosketch=models.FileField(upload_to='files/')
    
    def __str__(self):
        return self.proposal_name 

#class Proposal(models.Model):








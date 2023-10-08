from django.db import models

# Create your models here.
class Participant(models.model):
    Participant_Type=[
        (Applicant,"applicant"),
        (Admin,"admin"),
    ]
    Participant_login=models.CharField(max_length=20,choices=Participant_Type,default=Applicant)
class Applicant(models.model):
    first_name=models.CharField(max_length=30,)
    middle_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30)
    reg_no=models.CharField(max_length=30,primary_key=True,unique=True)
    email_address=models.EmailField(max_length=254,unique=True)
    phone_number=models.IntegerField(max_length=15,unique=True)
    password=models.CharField(max_length=15,unique=True)
    gender=models.CharField(max_length=15)  
    Type_of_Proposal=models.CharField(max_length=5,choices=Proposal_Type,default=Sonas)
    Proposal_Type=[
        (Sonas,"Sonas"),
        (Sass,"Sass"),
    ]
    


class Admin(models.model):
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30)
    email_address=models.EmailField(max_length=254)
    password=models.CharField(max_length=15)
    Type_of_Admin=models.CharField(max_length=5,choices=Admin_Type,default=Sonas)
    Admin_Type=[
        (Sonas,"sonas"),
        (Sass,"sass"),
    ]

class SassProposal(models.model):
    Problem_identification=models.TextField(max_length=1000)
    Research_purpose=models.TextField(max_length=800)
    Project_design=models.TextField(max_length=1000)
    Gender_equality=models.TextField(max_length=500)
    Research_ethics=models.Textfield(max_length=500)
    Critical_risks=models.TextField(max_length=500)
    Monitoring_Evaluation=models.TextField(max_length=700)
    Project_Team=models.TextField(max_length=500)

class SonasProposal(models.model):
    Personal_statement=models.Textfield(max_length=799)
    Research_Proposal=models.TextField(max_length=999)
    Research_environment=models.TextField(max_length=500)
    Research_Team_Capacity=models.TextField(max_length=500)
    IRB_Ethics=models.TextField(max_length=299)
    Additional_funding=models.TextFIeld(max_length=299)
    Project_Timeline=models.TextField(max_length=499)
    Budget=models.TextField(max_length=499)
    NHIF_Biosketch=models.FieldFle()







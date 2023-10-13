from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
#from django.contrib.auth import get_user_model


# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email



class user_type(models.Model):
    is_teach = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
         if self.is_student == True:
             return User.get_email(self.user) + " - is_student"
         else:
             return User.get_email(self.user) + " - is_teacher"


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
    NHIF_Biosketch=models.FileField()

#class Proposal(models.Model):







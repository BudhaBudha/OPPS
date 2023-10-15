from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SassForm(ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = SassProposal
 
        # specify fields to be used
        fields = '__all__'

class SonasForm(ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = SonasProposal
 
        # specify fields to be used
        fields = '__all__'

class CreateUserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
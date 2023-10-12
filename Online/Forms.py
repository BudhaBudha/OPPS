from django import forms
from .models import *

class SassForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = SassProposal
 
        # specify fields to be used
        fields = '__all__'

class SonasForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = SonasProposal
 
        # specify fields to be used
        fields = '__all__'
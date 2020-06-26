from django import forms
from django.forms import ModelForm
from .models import *

class CrudForm(forms.ModelForm):

    class Meta:
        model = Crud
        fields = '__all__' 
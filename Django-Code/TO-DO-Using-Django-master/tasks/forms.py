from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    # step 15 :

    class Meta:
        model = Task # this is the model
        fields = '__all__' # allow all the fields of that form


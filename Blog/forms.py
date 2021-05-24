from django import forms
from django.forms.models import ModelForm
from .models import *

class Postform(ModelForm):
    class Meta :
        model = post
        fields = "__all__"
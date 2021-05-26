from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class Postform(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta :
        model = post
        fields = "__all__"
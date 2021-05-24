from django.shortcuts import render,redirect
from .models import question

# Create your views here.
def home(request):
    poll = question.objects.all()
    context = {'poll': poll}
    return render(request ,'home.html', context= context)
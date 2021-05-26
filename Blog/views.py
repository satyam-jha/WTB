from django.shortcuts import redirect, render
from .models import *
from .forms import Postform
# Create your views here.

def home(request):
    blogs = post.objects.all( )
    authors = author.objects.all( )
    context = { 'blogs': blogs ,
                'authors': authors , }
    
    return render(request,'home.html',context=context)


def author_details(request,pk):
    authors = author.objects.get(name = pk)
    context = {'authors':authors}

    return render(request, 'author.html' , context=context)

def article(request,pk):
    blog = post.objects.get(title = pk.replace('-' , ' '))
    context = { 'blog':blog }

    return render(request, 'article.html', context=context)

def edit(request,pk):
    blog = post.objects.get(title = pk.replace('-' , ' '))
    form = Postform(instance=blog)
    if request.method == 'POST' :
        form = Postform(request.POST , instance= blog)
        if form.is_valid() :
            form.save()
            link = form.cleaned_data.get("title")
            return redirect('article', pk = link.replace(' ', '-'))
    context = {'blog': blog,
                'form' : form} 

    return render(request , 'write.html' , context = context)
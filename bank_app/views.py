from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from .models import Branch,Blog


def home(request,c_slug=None):
    data=None
    blog = Blog.objects.all()
    branch = Branch.objects.all()
    for i in branch:
        print(i)
    return render(request, 'index.html',{'branches': branch,"blogs":blog})



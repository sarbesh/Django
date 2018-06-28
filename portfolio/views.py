from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from portfolio.models import Name

# Create your views here.
def index(request):
    context={}
    return render(request,'portfolio/base.html')

def my(request, slug):
    profiledata = get_object_or_404(Name, slug=slug)
    context = {'data': profiledata}
    return render (request,"portfolio/my.html", context)

def sarbesh(request):
    return render(request,'portfolio/portfolio.html')

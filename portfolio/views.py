from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Name

# Create your views here.
def index(request):
    context={}
    return render(request,'portfolio/base.html')

def my(request):
	return render(request,'portfolio/my.html')

def sarbesh(request):
    return render(request,'portfolio/portfolio.html')

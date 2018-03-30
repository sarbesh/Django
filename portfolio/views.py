from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'portfolio/base.html')

def sarbesh(request):
    return render(request,'portfolio/portfolio.html')

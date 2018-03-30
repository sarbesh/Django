from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'portfolio/base.html')

def hello(request):
    return HttpResponse("<h1>This is my portfolio page</h1>")

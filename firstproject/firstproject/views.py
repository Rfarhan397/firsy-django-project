
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return HttpResponse ("hello")
def temp(request):
     return render(request,'basic.html')
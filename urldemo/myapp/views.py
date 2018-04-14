from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def fun(request):
    #return HttpResponse("fun()...")
    return redirect(reverse('index'))

def fun2(request,num,name):
    return HttpResponse("fun()....%s %s"%(num,name))

def fun3(request,yy,name):
    return HttpResponse("fun()....%s %s"%(yy,name))
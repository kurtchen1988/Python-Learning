from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request, arg1):
    return HttpResponse("我是blog的网页2")
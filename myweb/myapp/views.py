from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu
# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def stu(request):
    mod = Stu.objects
    list = mod.all()
    print(list)

    return HttpResponse("OK")
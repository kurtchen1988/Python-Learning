from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from myapp.models import District

# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def demo1(request):
    context={}
    context['name']="ZhangSan"
    context['a']=[10,20,30]
    context['stu']={"name":"lisi","age":20}
    data=[
        {"name":"zhangsuici","sex":1,"age":40,"state":0},
        {"name":"duanlili","sex":0,"age":38,'state':2},
        {"name":"wulizhang","sex":1,"age":20,'state':1},
        {"name":"zhaomin","sex":0,"age":18,'state':2}
    ]
    context['dlist']=data
    context['time']=datetime.now
    context['m1']=100
    context['m2']=20
    return render(request,"myapp/demo1.html",context)

def demo2(request):
    return render(request,"myapp/demo2.html")

def showdistrict(request):
    return render(request,"myapp/district.html")

def district(request,upid):
    dlist = District.objects.filter(upid=upid)
    list = []
    for ob in dlist:
        list.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list})
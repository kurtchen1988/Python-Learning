from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Photos
from datetime import datetime
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import time,os
from PIL import Image
# Create your views here.
def index(request):
    '''

    :param request:
    :return: 返回到图片展示页面的第一页
    '''
    return render(request,"index.html")

def showpic(request):
    '''

    :param request: 网页响应参数
    :return: 返回到相册添加页面
    '''
    return render(request, "myapp/add.html")

def piclist(request, pIndex):
    '''

    :param request: 网页响应参数
    :param pIndex:
    :return:
    '''
    use=Photos.objects.all()
    list = Photos.objects.all()
    p = Paginator(list, 5)
    if pIndex == ":":
        pIndex = "1"
    list2 = p.page(pIndex)
    context = {"ulist": list}
    plist = p.page_range
    context = {"ulist": list2, "plist": plist, "pIndex": int(pIndex)}
    return render(request, 'myapp/index.html', context)

def delpic(request, pIndex):


    pass

def editpic(request, pIndex):
    '''
    加载相册修改信息
    :param request:
    :param pIndex:
    :return:
    '''
    if pIndex == ":":
        return HttpResponse("没有上传文件信息")
    print(pIndex)
    plist = Photos.objects.get(id=int(pIndex))
    context = {"plist":plist}
    return render(request,"myapp/modify.html",context)

@csrf_exempt
def subeditpic(request):
    '''
    执行修改相册信息
    :param request:
    :return:
    '''
    print(request.POST['id'])
    ob = Photos.objects.get(id=request.POST['id'])
    ob.name = request.POST['title']
    ob.pic = request.POST['pic']
    ob.save()
    return HttpResponseRedirect("piclist/1")

@csrf_exempt
def addpic(request):
    '''
    添加图片功能
    :param request: 网页响应参数
    :return: 返回到图片展示页面的第一页
    '''
    #首先上传文件到相应目录（要确保static/pictures这个目录在项目根目录下，并且有读写权限）
    myfile = request.FILES.get("mypic", None)
    print(myfile)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pictures/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    #接着把所有信息写入数据库，图片仅存名字
    ob = Photos()
    ob.title = request.POST['title']
    ob.pic = filename
    ob.timeupload = datetime.now()

    ob.save()

    return HttpResponseRedirect("piclist/1")

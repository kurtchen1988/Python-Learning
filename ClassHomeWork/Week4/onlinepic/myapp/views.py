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
    图片展示页方法
    :param request: 网页响应参数
    :return: 返回到图片展示页面的第一页
    '''
    return render(request,"index.html")

def showpic(request):
    '''
    图片添加展示页方法
    :param request: 网页响应参数
    :return: 转到相册添加方法
    '''
    return render(request, "myapp/add.html")

def piclist(request, pIndex):
    '''
    图片页码方法
    :param request: 网页响应参数
    :param pIndex: 页码数
    :return: 转到相应的页码页面
    '''
    list = Photos.objects.get_queryset().order_by('id')
    p = Paginator(list, 5) # 一页显示五个图片信息
    if pIndex == ":":
        pIndex = "1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"ulist": list2, "plist": plist, "pIndex": int(pIndex)}
    return render(request, 'myapp/index.html', context)

def delpic(request, pIndex):
    '''
    图片删除方法
    :param request: 网页响应参数
    :param pIndex: 图片的ID
    :return: 转入信息提示页；如果成功删除返回代码1；如果失败删除返回代码2
    '''
    try:
        ob = Photos.objects.get(id=int(pIndex))
        ob.delete()
        return HttpResponseRedirect("../info/1")
    except Exception as err:
        print(err)
        return HttpResponseRedirect("../info/2")

def editpic(request, pIndex):
    '''
    加载相册修改信息
    :param request:
    :param pIndex: 图片的ID
    :return: 转入执行修改方法
    '''
    plist = Photos.objects.get(id=int(pIndex))
    context = {"plist":plist}
    return render(request,"myapp/modify.html",context)

@csrf_exempt
def addpic(request):
    '''
    添加图片功能
    :param request: 网页响应参数
    :return: 转入信息提示页；如果成功添加返回代码3；如果失败添加返回代码4
    '''
    #首先上传文件到相应目录（要确保static/pictures这个目录在项目根目录下，并且有读写权限）
    try:
        myfile = request.FILES.get("mypic", None)
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

        return HttpResponseRedirect("../info/3")
    except Exception as error:
        print(error)
        return HttpResponseRedirect("../info/4")

@csrf_exempt
def subeditpic(request):
    '''
    执行修改相册信息
    :param request: 网页响应参数
    :return: 转入信息提示页；如果成功修改返回代码5；如果失败修改返回代码6
    '''
    try:
        ob = Photos.objects.get(id=request.POST['id'])
        ob.name = request.POST['title']
        ob.pic = request.FILES.get("mypic", None)
        ob.save()
        return HttpResponseRedirect("../info/5")
    except Exception as error:
        print(error)
        return HttpResponseRedirect("../info/6")

def info(request, inID):

    if int(inID) == 1:
        context = {'info':'已成功删除图片！'}
        return render(request, "myapp/info.html", context)
    elif int(inID) == 2:
        context = {'info': '抱歉，未能成功删除图片！'}
        return render(request, "myapp/info.html", context)
    elif int(inID) == 3:
        context = {'info': '已成功添加图片！'}
        return render(request, "myapp/info.html", context)
    elif int(inID) == 4:
        context = {'info': '抱歉，未能成功添加图片！'}
        return render(request, "myapp/info.html", context)
    elif int(inID) == 5:
        context = {'info': '已成功修改图片！'}
        return render(request, "myapp/info.html", context)
    elif int(inID) == 6:
        context = {'info': '抱歉，未能成功修改图片！'}
        return render(request, "myapp/info.html", context)


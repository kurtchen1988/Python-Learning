from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
from django.views.decorators.csrf import csrf_exempt
import time,os
from PIL import Image
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def demo1(request):
    '''加载上传表单'''
    return render(request,"myapp/demo1.html")

@csrf_exempt  
def upload(request):
    '''执行图片的上传'''
    myfile = request.FILES.get("mypic",None)
    print(myfile)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time())+"."+myfile.name.split('.').pop()
    destination = open("./static/pics/"+filename,"wb+")
    for chunk in myfile.chunks():      # 分块写入文件  
        destination.write(chunk)  
    destination.close()

    # 执行图片缩放
    im = Image.open("./static/pics/"+filename)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用jpeg格式保存: 
    im.save("./static/pics/s_"+filename,None)

    return HttpResponse("ok")

def demo2(request,pIndex):
    list = Users.objects.all()
    p = Paginator(list,4)
    if pIndex == "":
    	pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"ulist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request, 'myapp/demo2.html',context)

def demo3(request):
    '''富文本编辑器'''
    return render(request,"myapp/demo3.html")

from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Photos
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import time,os
from PIL import Image
# Create your views here.
def index(request):
    return render(request,"index.html")

def showpic(request):
    return render(request, "myapp/add.html")

def piclist(request, pIndex):
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

@csrf_exempt
def addpic(request):
    myfile = request.FILES.get("mypic", None)
    print(myfile)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pictures/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    # 执行图片缩放
    im = Image.open("./static/pics/" + filename)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用jpeg格式保存:
    im.save("./static/pics/s_" + filename, None)

    return HttpResponse("ok")

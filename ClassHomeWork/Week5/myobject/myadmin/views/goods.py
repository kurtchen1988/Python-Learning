from django.shortcuts import render
from django.http import HttpResponse

from common.models import Goods,Types
from datetime import datetime
from PIL import Image
import time
# Create your views here.
def index(request):
    '''浏览信息'''
    list = Goods.objects.all()
    #遍历商品信息，并获取对应的商品类别名称，以typename名封装
    for vo in list:
        ty = Types.objects.get(id=vo.typeid)
        vo.typename = ty.name
    context = {"goodslist":list}
    return render(request,"myadmin/goods/index.html",context)

def add(request):
    '''加载添加页面'''
    #获取商品类别信息
    tlist = Types.objects.extra(select={'_has':'concat(path,id)'}).order_by('_has')
    for ob in tlist:
        ob.pname = '. . .'*(ob.path.count(',')-1)
    context={'typelist':tlist}
    return render(request,"myadmin/goods/add.html",context)

def insert(request):
    '''执行添加'''
    try:
        # 图片的上传处理
        myfile = request.FILES.get("pic",None)
        if not myfile:
            return HttpResponse("没有上传文件信息")
        filename = str(time.time())+"."+myfile.name.split('.').pop()
        destination = open("./static/goods/"+filename,"wb+")
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        # 图片的缩放
        im = Image.open("./static/goods/"+filename)
        # 缩放到375*375(缩放后的宽高比例不变):
        im.thumbnail((375, 375)) 
        im.save("./static/goods/"+filename,None)
        
        im = Image.open("./static/goods/"+filename)
        # 缩放到220*220(缩放后的宽高比例不变):
        im.thumbnail((220,220)) 
        im.save("./static/goods/m_"+filename,None)

        im = Image.open("./static/goods/"+filename)
        # 缩放到75*75(缩放后的宽高比例不变):
        im.thumbnail((75, 75)) 
        im.save("./static/goods/s_"+filename,None)

        #保存商品信息
        ob = Goods()
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.content = request.POST['content']
        ob.picname = filename
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"添加成功！"}
    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,"myadmin/info.html",context)

def delete(request,tid):
    '''删除信息'''
    try:
        ob = Goods.objects.get(id=tid)
        ob.delete()
        context={"info":"删除成功！"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,"myadmin/info.html",context)


def edit(request,tid):
    '''加载编辑信息页面'''
    try:
        ob = Goods.objects.get(id=tid)
        context={"goods":ob}
        return render(request,"myadmin/goods/edit.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,tid):
    '''执行编辑信息'''
    try:
        ob = Goods.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    return render(request,"myadmin/info.html",context)
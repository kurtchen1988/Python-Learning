from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
from common.models import Users
# Create your views here.
def index(request, pIndex):
    '''浏览信息'''
    list = Users.objects.get_queryset().order_by('id')
    p = Paginator(list, 5)  # 一页显示五个用户信息
    if pIndex == ":":
        pIndex = "1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"userslist":list2, "plist":plist,"pIndex":int(pIndex)}
    return render(request,"myadmin/users/index.html",context)

def add(request):
    '''加载添加页面'''
    return render(request,"myadmin/users/add.html")

def insert(request):
    '''执行添加'''
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"添加成功！"}
    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,"myadmin/info.html",context)

def delete(request,uid):
    '''删除信息'''
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context={"info":"删除成功！"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,"myadmin/info.html",context)


def edit(request,uid):
    '''加载编辑信息页面'''
    try:
        ob = Users.objects.get(id=uid)
        context={"user":ob}
        return render(request,"myadmin/users/edit.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,uid):
    '''执行编辑信息'''
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    return render(request,"myadmin/info.html",context)

def passch(request, uid):
    try:
        ob = Users.objects.get(id = uid)
        context = {"user":ob}
        return render(request, "myadmin/users/passchan.html",context)
    except Exception as err:
        print(err)
        context = {"info":"没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)

def passup(request,uid):
    try:
        ob = Users.objects.get(id = uid)
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password1'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.save()
        context = {"info": "用户密码修改成功！"}
        return render(request, "myadmin/info.html", context)
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)

def search(request):
    print(request.POST['keyword'])
    try:
        list = Users.objects.filter(name=request.POST.get('keyword'))
        if(list != None):
            p = Paginator(list, 5)  # 一页显示五个用户信息
            list2 = p.page(1)
            plist = p.page_range
            context = {"userslist": list2, "plist": plist, "pIndex": 1}
            return render(request, "myadmin/users/index.html", context)
        else:
            context = {"info": "无搜索结果！"}
            return render(request, "myadmin/info.html", context)

    except Exception as err:
        context = {"info": "搜索出错！"}
        return render(request, "myadmin/info.html", context)
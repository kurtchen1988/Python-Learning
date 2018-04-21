from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users
from datetime import datetime
# Create your views here.
def index(request):
    '''浏览信息'''
    list = Users.objects.all()
    context = {"userslist":list}
    return render(request,"myadmin/users/index.html", context)

def add(request):
    '''加载添加页面'''
    return render(request,"myadmin/users/add.html")

def insert(request):
    '''执行添加'''
    try:
        ob = Users()
        ob.username = request.POST["username"]
        ob.name = request.POST["name"]
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        #ob.password = request.POST["password"]
        ob.sex = request.POST["sex"]
        ob.address = request.POST["address"]
        ob.code = request.POST["code"]
        ob.phone = request.POST["phone"]
        ob.email = request.POST["email"]
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "添加成功"}
    except Exception as err:
        print(err)
        context = {"info":"添加失败"}
    return render(request,"myadmin/info.html", context)

def delete(request, uid):
    '''删除信息'''
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context = {"info": "删除失败"}
    return render(request, "myadmin/info.html", context)

def edit(request, uid):
    '''加载编辑信息页面'''
    try:
        ob = Users.objects.get(id=uid)
        context = {"user": ob}
        return render(request, "myadmin/users/edit.html", context)
    except Exception as err:
        context = {"info": "没有找到要修改的信息"}
        return render(request, "myadmin/info.html", context)

def update(request, uid):
    '''执行编辑信息'''
    try:
        ob = Users.objects.get(id = uid)
        ob.name = request.POST["name"]
        #ob.password = request.POST["password"]
        ob.sex = request.POST["sex"]
        ob.address = request.POST["address"]
        ob.code = request.POST["code"]
        ob.phone = request.POST["phone"]
        ob.email = request.POST["email"]
        ob.state = request.POST["state"]
        ob.save()
        context = {"info": "修改成功"}
    except Exception as err:
        print(err)
        context = {"info":"修改失败"}
    return render(request,"myadmin/info.html", context)
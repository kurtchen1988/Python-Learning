from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def indexUsers(request):
    list = Users.objects.all()
    context = {"userslist":list}
    return render(request,"myapp/users/index.html",context)

def addUsers(request):
    return render(request,"myapp/users/add.html")

def insertUsers(request):
    try:
        user = Users()
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.addtime = datetime.now()
        user.save()
        context = {"info":"添加成功！"}
    except:
        context = {"info":"添加失败！"}

    return render(request,"myapp/users/info.html",context)

def delUsers(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info":"用户删除成功！"}
    except:
        context = {"info":"用户删除失败！"}
    return render(request,"myapp/users/info.html",context)

def editUsers(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        context ={"user":ob}
        return render(request,"myapp/users/edit.html",context)
    except Exception as err:
        print(err)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"myapp/users/info.html",context)

def updateUsers(request):
    try:
        user = Users.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.addtime = datetime.now()
        user.save()
        context = {"info":"修改成功！"}
    except:
        context = {"info":"修改失败！"}

    return render(request,"myapp/users/info.html",context)
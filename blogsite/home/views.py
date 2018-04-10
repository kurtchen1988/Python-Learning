from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usermsg
from .models import Typemsg
from .models import Article

# Create your views here.
def article(request):
    pass

def reg(request):
    if request.session.has_key("name617826782"):
        return HttpResponseRedirect("/")
    if request.method=="POST":
        name=request.POST["name"]
        passwd=request.POST["passwd"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        Usermsg.objects.create(name=name, passwd=passwd, email=email, phone=phone, isadmin=0)
        return HttpResponse("注册成功")
    return render(request,"reg.html")

def login(request):
    if request.session.has_key("name617826782"):
        return HttpResponseRedirect("/")
    if request.method=="POST":
        name=request.POST["name"]
        passwd=request.POST["passwd"]
        islogin=Usermsg.objects.filter(name__exact=name,passwd__exact=passwd)
        if islogin:
            request.session["name617826782"]=name
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("登录失败")
    return render(request,"login.html")

def logout(request):
    del request.session["name617826782"]
    return HttpResponseRedirect("/")

def index(request):
    if request.session.has_key("name617826782"):
        nav1=request.session["name617826782"]
        nav2="/"
        nav3="退出"
        nav4="/logout"
    else:
        nav1="注册"
        nav2="/reg2"
        nav3="登录"
        nav4="/login"
    typename=Typemsg.objects.values("id","typename")
    article=Article.objects.values("id", "title", "author", "detail")[:20]
    return render(request,"index.html",{"article":article,"typename":typename,"nav1":nav1,"nav2":nav2,"nav3":nav3,"nav4":nav4})

    #return render(request,"index.html")

def alist(request):
    pass

def postarticles(request):
    pass
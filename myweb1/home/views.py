from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Usermsg
from .form import RegisterForm
# Create your views here.
def Useradd(request):
    alluser = ["黎明", "张军", "大胡", "李伟", "杨明"]
    for i in alluser:
         Usermsg.objects.create(name=i,passwd="weijc7789",email="qwe@qq.com",phone=123456,isadmin=True)
    return HttpResponse("插入成功")

def Userfind(request):
    #rst=Usermsg.objects.values("id","name","email","phone")
    #rst=list(Usermsg.objects.filter(name="张军").values())[0]["id"]
    #rst=Usermsg.objects.filter(name="杨明").update(email="12345@qwe.com")
    rst=Usermsg.objects.filter(name__exact="张军",passwd__exact="weijc7789")
    return HttpResponse(rst)

def first(request):
    #这里写入代码，这样可以处理相应数据
    a=9
    b=10
    c=a+b
    return HttpResponse("欢迎来到韦老师课堂"+str(c))

def test(request):
    #return HttpResponse("我是home的网页2")
    #return HttpResponseRedirect("/first")
    a=9
    b=7
    c=a+b
    name = ["<b>黎明</b>","<b>张军</b>","<b>大胡</b>","<b>李伟</b>","<b>杨明</b>"]
    sex = ["男","男","女","女","男"]
    name_sex=zip(name, sex)
    return render(request,"test.html", {"name_sex":name_sex, "sex":sex,"name":name, "title":"测试页面","a":str(a),"b":str(b),"c":str(c)})

def article(request, id):
    title="Python爬虫路线"
    content="<br>Python爬虫路线Python爬虫路线Python爬虫路线Python爬虫路线Python爬虫路线Python爬虫路线Python爬虫路线</br>"
    return render(request,"article.html",{"title":title, "content":content})

def add(request, add1, add2):
    rst=int(add1)+int(add2)
    return HttpResponse(str(add1)+"+"+str(add2)+"的结果是"+str(rst))
'''xxxx.com/add2/?add1=xxx&add2=xxx'''

def add2(request):
    a=request.GET["add1"]
    b=request.GET["add2"]
    c=int(a)+int(b)
    return HttpResponse(str(a)+"+"+str(b)+"的结果是"+str(c))

def reg1(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            passwd=form.cleaned_data["passwd"]
            email=form.cleaned_data["email"]
            phone=form.cleaned_data["phone"]
            Usermsg.objects.create(name=name,passwd=passwd,email=email,phone=phone,isadmin=0)
            return HttpResponse("注册成功！"+str(name)+","+str(passwd)+","+str(email)+","+phone)
    else:
        form=RegisterForm()
    return render(request,"reg1.html",{"form":form})

def reg2(request):
    if request.session.has_key("name617826782"):
        return HttpResponseRedirect("/")
    if request.method=="POST":
        name=request.POST["name"]
        passwd=request.POST["passwd"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        Usermsg.objects.create(name=name, passwd=passwd, email=email, phone=phone, isadmin=0)
        return HttpResponse("传递过来的信息是" + str(name) + "," + str(passwd) + "," + str(email) + "," + phone)
    return render(request,"reg2.html")

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
    return render(request,"index1.html",{"nav1":nav1,"mav2":nav2,"nav3":nav3,"nav4":nav4})
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
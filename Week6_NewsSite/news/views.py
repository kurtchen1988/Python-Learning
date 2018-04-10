from django.shortcuts import render
from .models import Usermsg
from .models import News
from .models import Newstype
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
#from vmOperation import operationVM
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
#集中伪静态化
def static_all(request, thepage):
    import urllib.request
    path = os.path.join(BASE_DIR, "templates/static_all/")
    for i in range(0,int(thepage)):
        try:
            url = "http://127.0.0.1:8000/news/" + str(i)
            urllib.request.urlretrieve(url, filename=path+str(i)+".html")
        except Exception as Err:
            print(Err)
    return HttpResponse("处理成功")

#登录
def login(request):
    if request.session.has_key("name122"):
        return HttpResponseRedirect("/")
    if request.method == "POST":
        name = request.POST["name"]
        passwd = request.POST["passwd"]
        islogin = Usermsg.objects.filter(name__exact=name, passwd__exact=passwd)
        if islogin:
            request.session["name122"]=name
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("")
    return render(request, "login.html")

#登出
def logout(request):
    del request.session["name122"]
    return HttpResponseRedirect("/")

#注册
def reg(request):
    if request.session.has_key("name122"):
        return HttpResponseRedirect("/")
    if request.method == "POST":
        name = request.POST["name"]
        passwd = request.POST["passwd"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        Usermsg.objects.create(name=name, passwd=passwd, email=email, phone=phone, isadmin=0)
        return HttpResponse("注册成功，用户名为: " + str(name) + "，信箱为:" + str(email) + "，电话为: " + str(phone)+"<br /><br /><a href = '/'>[返回-首页]</a>")
    else:
        pass
    return render(request, "reg.html")

#首页
def index(request):
    if request.session.has_key("name122"):
        nav1 = request.session["name122"]
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
        # return HttpResponseRedirect("/")
    else:
        nav1 = "注册"
        nav2 = "/reg"
        nav3 = "登录"
        nav4 = "/login"
    typename = Newstype.objects.values("id", "typename")
    news = News.objects.values("id", "title", "author", "detail", "content")[:10]

    #首页的分页处理
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        newspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        newspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        newspage = paginator.page(paginator.num_pages)
    return render(request, "index.html",
                  {"newspage": newspage, "news": news, "typename": typename, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})

#新闻浏览
def news(request, nid):
    path = os.path.join(BASE_DIR, "templates/static_all/")
    if os.path.exists(path+str(nid)+".html"):
        return render(request, path+str(nid)+".html")
    else:
        thisnews = list(News.objects.filter(id=nid).values("id", "title", "author", "content"))[0]
        return render(request, "news.html", {"thisnews": thisnews, })

#新闻列表
def alist(request):
    if request.session.has_key("name122"):
        nav1 = request.session["name122"]
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
        # return HttpResponseRedirect("/")
    else:
        nav1 = "注册"
        nav2 = "/reg"
        nav3 = "登录"
        nav4 = "/login"
    category = Newstype.objects.values("id", "typename")
    news = News.objects.values("id", "title", "author", "detail", "content")
    return render(request, "list.html",
                  {"news": news, "category": category, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})

#按新闻类别浏览
def category(request,tid):
    if request.session.has_key("name122")==False:
        return HttpResponseRedirect("/login")
    else:
        nav1 = request.session["name122"]
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    thisnews = list(News.objects.filter(tid=tid).values("id", "title", "author", "detail", "content"))
    thiscategory = list(Newstype.objects.filter(id=tid).values("id", "typename"))[0]
    return render(request, "category.html", {"thisnews": thisnews, "thiscategory": thiscategory, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})

#发新闻
def postnews(request):
    if request.session.has_key("name122")==False:
        return HttpResponseRedirect("/login")
    else:
        nav1 = request.session["name122"]
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    typeall = Newstype.objects.values("id", "typename")
    typeid = []
    typename = []
    for item in typeall:
        typeid.append(item["id"])
        typename.append(item["typename"])
    typeidandname = zip(typeid, typename)

    user = list(Usermsg.objects.filter(name=request.session["name122"]).values())[0]
    uid = user["id"]
    uname = user["name"]
    isadmin = user["isadmin"]
    if (not isadmin):
        return HttpResponseRedirect("/")
    if request.method == "POST":
        content = request.POST["content"]
        thistypeid = request.POST["typeid"]
        postname = request.POST["title"]
        detail = request.POST["detail"]
        News.objects.create(title=postname, content=content, tid=thistypeid, uid=uid, author=uname, detail=detail)
        return HttpResponseRedirect("/")
    return render(request, "postnews.html", {"typeidandname":typeidandname, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})

#分页
def page(request,pid):
    if request.session.has_key("name122"):
        nav1 = request.session["name122"]
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        nav1 = "注册"
        nav2 = "/reg"
        nav3 = "登录"
        nav4 = "/login"
    #pid = re.sub("\D", "", pid)
    currentpage = int(pid[0])
    i = (int(currentpage)-1)*10
    j = int(currentpage)*10
    typename = Newstype.objects.values("id", "typename")
    news = News.objects.values("id", "title", "author", "detail", "content")[i:j]

    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)  # Show 10 contacts per page

    page = currentpage
    try:
        newspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        newspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        newspage = paginator.page(paginator.num_pages)
    return render(request, "p.html",
                  {"page":page, "newspage": newspage, "news": news, "typename": typename, "nav1": nav1, "nav2": nav2, "nav3": nav3,
                   "nav4": nav4})

#调用封装的XenServer SDK并在页面显示Demo
'''
def xenstatus(request, vid):
    xenStatus = operationVM(vid)
    return render(request, "xenserver.html", {"xenStatus": xenStatus,})
'''
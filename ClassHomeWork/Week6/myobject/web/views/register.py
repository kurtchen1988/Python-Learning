from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.core.paginator import Paginator

from common.models import Users,Types,Goods,Orders,Detail


def regist(request):
    '''
    转到注册页面
    :param request:
    :return: 转到注册页面
    '''
    return render(request,"web/register.html")

def addvip(request):
    '''
    前台用户添加
    :param request:
    :return: 转到注册页面，带信息
    '''
    verifycode = request.session['verifycode']
    code = request.POST['code']
    passwd = request.POST['password']
    passwd2 = request.POST['password2']
    # 检查验证码是否正确
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "web/register.html", context)
    # 检查两次输入密码是否正确
    if passwd != passwd2:
        context = {'info':'两次输入密码不相同，请再次输入！'}
        return render(request,"web/register.html", context)

    try:
        user = Users()
        user.username = request.POST['username']
        import hashlib
        m = hashlib.md5()
        m.update(bytes(passwd,encoding="utf8"))
        user.password = m.hexdigest()
        user.save()
        context = {'info':"注册成功，请点击登录！"}
    except:
        context = {'info': '注册账号错误！'}
    return render(request, "web/register.html", context)
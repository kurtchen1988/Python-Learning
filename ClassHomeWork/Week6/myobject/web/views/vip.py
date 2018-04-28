from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.core.paginator import Paginator

from common.models import Users,Types,Goods,Orders,Detail

# 公共信息加载函数
def loadinfo(request):
    lists = Types.objects.filter(pid=0)
    context = {'typelist':lists}
    return context

def  viporders(request):
    '''浏览订单信息'''
    context = loadinfo(request)
    #获取当前登录者的订单信息
    odlist = Orders.objects.filter(uid=request.session['vipuser']['id'])
    #遍历订单信息，查询对应的详情信息
    for od in odlist:
        delist = Detail.objects.filter(orderid=od.id)
        #遍历订单详情，并且获取对应的商品信息（图片）
        for og in delist:
            og.picname = Goods.objects.only("picname").get(id=og.goodsid).picname
        od.detaillist = delist

    context['orderslist'] = odlist
    return render(request,"web/viporders.html",context)

def odstate(request):
    ''' 修改订单状态 '''
    try:
        oid = request.GET.get("oid",'0')
        ob = Orders.objects.get(id=oid)
        ob.state = request.GET['state']
        ob.save()
        return redirect(reverse('vip_orders'))
    except Exception as err:
        print(err)
        return HttpResponse("订单处理失败！")

def info(request):
    user = Users.objects.filter(id = request.session['vipuser']['id'])
    context = {'user':user}
    return render(request,'web/vipinfo.html', context)

def update(request):
    try:
        user = Users.objects.get(id = request.session['vipuser']['id'])
        user.name = request.POST['name']
        user.sex = request.POST['sex']
        user.phone = request.POST['phone']
        user.address = request.POST['address']
        user.code = request.POST['code']
        user.email = request.POST['email']
        user.save()
        context = {'info': '您的会员信息修改成功!'}
    except Exception as err:
        print(err)
        context = {'info' : '您的会员信息修改失败！'}
    return render(request,'web/vipinfo.html', context)

def resetps(request):
    pass

def doresetps(request):
    pass

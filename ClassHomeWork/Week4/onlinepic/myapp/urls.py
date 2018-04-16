from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    #进入系统首页
    url(r'^$',views.index, name='index'),
    # 进入相册列表页
    url(r'^piclist/(?P<pIndex>[0-9]+)$',views.piclist, name='piclist'),
    # 文件上传展示
    url(r'^showpic$', views.showpic, name="showpic"),
    # 执行文件上传
    url(r'^upload$', views.addpic, name="upload"),
    # 删除图片
    url(r'delpic/(?P<pIndex>[0-9]+)$',views.delpic,name='delpic'),
    # 修改图片
    url(r'editpic/(?P<pIndex>[0-9]+)$',views.editpic,name='editpic'),
    # 执行修改图片信息
    url(r'modify$',views.subeditpic,name='subeditpic'),
    # 信息展示
    url(r'info/(?P<inID>[0-9]+)', views.info, name='info'),

]
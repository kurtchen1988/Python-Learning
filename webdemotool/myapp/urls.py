from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),

    #文件上传
    url(r'^showpic$', views.showpic, name="showpic"),
    url(r'^upload$', views.upload, name="upload"),

    #数据分页
    url(r'^demo2/(?P<pIndex>[0-9]+)$', views.demo2, name="demo2"),

    #富文本编辑器
    url(r'^demo3$', views.demo3, name="demo3"),
]
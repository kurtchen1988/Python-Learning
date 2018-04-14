from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^demo1$', views.demo1, name="demo1"),
    url(r'^demo2$', views.demo2, name="demo2"),
    url(r'^showdistrict$', views.showdistrict,name='showdistrict'),
    url(r'^district/([0-9]+)$',views.district,name='district'),
]
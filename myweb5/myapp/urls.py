from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^rp/(?P<cn>[a-z])$', views.rpdemo, name="rpdemo"),
    url(r'^rq$',views.rqdemo,name="rqdemo"),
    url(r'^verifycode$',views.verifycode,name="verifycode"),
]
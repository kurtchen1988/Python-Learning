from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^fun/2018',views.fun, name="fun"),
    url(r'^fun2/([0-9]{4})/([a-z]+)$',views.fun2),
    url(r'^fun3/(?P<yy>[0-9]{4})/(?P<name>[a-z]+)$',views.fun3)
]
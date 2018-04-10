"""Week6_NewsSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from news import views as news_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #管理后台
    url(r'^admin/', admin.site.urls),
    #登录/登出
    url(r'^login$', news_views.login),
    url(r'^logout$', news_views.logout),
    #注册
    url(r'^reg$', news_views.reg),
    #浏览新闻
    url(r'^news/(.*?)$', news_views.news),
    #新闻列表
    url(r'^list$', news_views.alist),
    #按新闻类别浏览
    url(r'^cate/(.*?)/$', news_views.category),
    #发布新闻
    url(r'^postnews$', news_views.postnews),
    #首页
    url(r'^$', news_views.index),
    #分页
    url(r'^page/(.*?)$', news_views.page),
    #伪静态化处理
    url(r'^static_all/(.*?)$',news_views.static_all),
    #调用XenServer SDK
    #url(r'^xenstatus/(.*?)$', news_views.xenstatus),
]

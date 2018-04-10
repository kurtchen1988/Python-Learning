"""myweb1 URL Configuration

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
from django.conf.urls import url #这个模块是视频中使用的模块，在现实中没有导入，必须手动导入
from home import views as home_views #通常情况下，会有很多个视图等等，这里就给它们重新命名，这样方便区别。通常名字为app名，下划线，加views
from blog import views as blog_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',home_views.first),
    #一定要注意，这一块与老师讲的不一样，要通过导入动作才能使用跟老师一样的
    url(r'^admin/',admin.site.urls),
    #url(r'^$', home_views.first),
    #这一块和视频里一模一样了就
    url(r'^first$', home_views.first), #这里配置的就是把带test的网址给
    url(r'^test.*?$',home_views.test),
    url(r'articles/(.*?)$',home_views.article),
    url(r'add/(.*?)/(.*?)$',home_views.add),
    url(r'^useradd$',home_views.Useradd),
    url(r'^userfind$',home_views.Userfind),
    url(r'^add2/.*?$',home_views.add2),
    url(r'^reg1$',home_views.reg1),
    url(r'^reg2$',home_views.reg2),
    url(r'^login$', home_views.login),
    url(r'^$',home_views.index),
    url(r'^logout$',home_views.logout),
]

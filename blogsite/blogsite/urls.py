"""blogsite URL Configuration

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
from django.conf.urls import url
from django.urls import path
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^articles/(.*?)$',home_views.article),
    url(r'^reg$',home_views.reg),
    url(r'^login$',home_views.login),
    url(r'^$', home_views.index),
    url(r'logout$',home_views.logout),
    url(r'^list$',home_views.alist),
    url(r'^postarticles$',home_views.postarticles),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}, name='static'),

]

from . import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^users$', views.indexUsers, name="users"),
    url(r'^users/add$', views.addUsers, name="addusers"),
    url(r'^users/insert$', views.insertUsers, name="insertusers"),
    url(r'^users/del/(?P<uid>[0-9]+)$', views.delUsers, name="delusers"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', views.editUsers, name="editusers"),
    url(r'^users/update$', views.updateUsers, name="updateusers"),

]
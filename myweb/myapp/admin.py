from django.contrib import admin
from myapp.models import Stu
# Register your models here.

@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','sex','classid')

    list_display_links = ('id','name')

    list_per_page = 10#每页显示多少条数据

    ordering = ('id',)#降序是用-id

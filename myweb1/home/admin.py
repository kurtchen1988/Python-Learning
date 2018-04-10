from django.contrib import admin
from .models import Usermsg
# Register your models here.
class UsermsgAdmin(admin.ModelAdmin):
    list_display = ("name","email")
admin.site.register(Usermsg, UsermsgAdmin)
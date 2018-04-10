from django.contrib import admin
from .models import News
from .models import Newstype
from .models import Usermsg

# Register your models here.
class UsermsgAdmin(admin.ModelAdmin):
    list_display = ("name","passwd","email","phone","isadmin")

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","author","detail","content", "uid","tid")

class NewstypeAdmin(admin.ModelAdmin):
    list_display = ("typename",)

admin.site.register(Usermsg, UsermsgAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Newstype, NewstypeAdmin)

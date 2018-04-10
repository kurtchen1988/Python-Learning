from django.db import models

'''
@一个类代表一个表
@其中ID，系统会默认生成，不需要手动处理
'''
# Create your models here
#用户信息表
class Usermsg(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    isadmin = models.BooleanField()

#新闻类型表 = 国内新闻，科技新闻，军事新闻...
class Newstype(models.Model):
    typename = models.CharField(max_length=50)

#新闻内容表
class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    content = models.TextField()
    uid = models.IntegerField()
    tid = models.IntegerField()

#评价表
class Comment(models.Model):
    uid = models.IntegerField()
    content = models.TextField()
    aid = models.IntegerField()
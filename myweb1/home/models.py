from django.db import models

# Create your models here.
'''
数据表------类
字段------类下面的一个属性
'''

class Usermsg(models.Model):
    name=models.CharField(max_length=50)
    passwd=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    isadmin=models.BooleanField()

class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    detail=models.TextField()
    content=models.TextField()
    uid=models.IntegerField()
    tid=models.IntegerField()

class Typemsg(models.Model):
    typename=models.CharField(max_length=50)

class Comment(models.Model):
    uid=models.IntegerField()
    content=models.TextField()
    aid=models.IntegerField()
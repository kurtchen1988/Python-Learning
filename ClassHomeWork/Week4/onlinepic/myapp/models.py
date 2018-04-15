from django.db import models
from datetime import datetime

# Create your models here.
class Photos(models.Model):
    title = models.CharField(max_length=150, default='pic')
    pic = models.CharField(max_length=250, default='pic')
    timeupload = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "%d:%s:%s:%s"%(self.id, self.title, self.pic, self.timeupload)
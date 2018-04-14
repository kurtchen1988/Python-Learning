from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255)
    upid = models.IntegerField()

    class Meta:
        db_table = "district"

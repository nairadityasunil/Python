from django.db import models

# Create your models here.
class emp(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
##
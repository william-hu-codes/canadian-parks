from django.db import models

# Create your models here.
class National_park(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
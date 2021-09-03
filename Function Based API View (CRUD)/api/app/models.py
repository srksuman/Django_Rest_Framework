from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    salary = models.BigIntegerField()
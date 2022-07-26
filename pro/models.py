from django.db import models

# Create your models here.

class Quest(models.Model):
    question = models.CharField(max_length=100)
    op1 = models.CharField(max_length=100,default=False)
    op2 = models.CharField(max_length=100,default=False)
    op3 = models.CharField(max_length=100,default=False)
    op4 = models.CharField(max_length=100,default=False)
    ans = models.CharField(max_length=100,default=False)

class User(models.Model):
    username = models.CharField(max_length=25,unique = True)
    password = models.CharField(max_length=25)
    result = models.PositiveIntegerField(default=0)

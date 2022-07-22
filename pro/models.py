from django.db import models

# Create your models here.

class Quest(models.Model):
    question = models.CharField(max_length=100)
    op1 = models.CharField(max_length=100,default=False)
    op2 = models.CharField(max_length=100,default=False)
    op3 = models.CharField(max_length=100,default=False)
    op4 = models.CharField(max_length=100,default=False)
    ans = models.CharField(max_length=100,default=False)
    result = models.PositiveIntegerField(default=0)

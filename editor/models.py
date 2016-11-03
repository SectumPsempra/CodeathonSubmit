from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    title = models.CharField(max_length=100,null=True)
    data = models.TextField(max_length=2000,null=True)
    number = models.IntegerField(null=True)
    answer = models.TextField(max_length=200,null=True)
    def __str__ (self):
        return str(self.number)

class User_db(models.Model):
    roll = models.OneToOneField(User)
    answer1 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer2 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer3 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer4 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer5 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer6 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer7 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer8 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer9 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer10 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer11 = models.TextField(max_length=1000,default="Enter Your Code Here")
    answer12 = models.TextField(max_length=1000,default="Enter Your Code Here")
    def __str__ (self):
        return str(self.roll)

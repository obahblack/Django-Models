from cgitb import text
from ssl import create_default_context
from statistics import mode
from turtle import title
from typing_extensions import Self
from django.db import models

# Create your models here.
user=input("Enter Author")
User = models.OneToOneField(user, null=True, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length= 200)
    text= models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.title
        

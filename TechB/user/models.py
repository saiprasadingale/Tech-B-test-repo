from django.db import models

# Create your models here.


class Usermodel(models.Model):
    username=models.CharField(max_length=50)
    task=models.TextField()
    time=models.TimeField(auto_now_add=True)
    date= models.DateField(auto_now_add=True)
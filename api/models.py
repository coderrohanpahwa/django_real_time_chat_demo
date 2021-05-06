from django.db import models

# Create your models here.
class Chat(models.Model):
    msg=models.CharField(max_length=100)
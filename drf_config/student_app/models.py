from django.db import models

# Create your models here.

# mode-->> serializer-->> view-->> template-->>

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)



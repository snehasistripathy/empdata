from django.db import models

# Create your models here.
class details(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Company = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Address = models.CharField(max_length=200)
    
    
    
    
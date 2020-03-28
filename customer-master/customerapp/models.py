from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name=models.CharField(max_length=30)
    customer_mobile_no=models.IntegerField()
    customer_age=models.FloatField()
    customer_city=models.CharField(max_length=30)

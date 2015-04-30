from django.db import models

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()
  description = models.TextField()
  imglink = models.CharField(max_length=100)


class Order(models.Model):
  total_price = models.FloatField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  address1 = models.CharField(max_length = 100)
  address2 = models.CharField(max_length = 100)
  city = models.CharField(max_length = 100)
  postcode = models.CharField(max_length = 10)
  payment_type = models.CharField(max_length = 50)
  payment_data = models.CharField(max_length = 100)
  items = models.TextField()
  fulfilled = models.BooleanField()

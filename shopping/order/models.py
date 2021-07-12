from django.contrib.auth.models import User
from django.db import models
from product.models import Product

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

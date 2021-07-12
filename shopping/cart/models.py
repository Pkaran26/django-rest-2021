from django.contrib.auth.models import User
from django.db import models
from product.models import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

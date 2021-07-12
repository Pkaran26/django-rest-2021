from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from order.models import Order

class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

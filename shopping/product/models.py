from django.contrib.auth.models import User
from django.db import models
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.TextField(null = True)
    description = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

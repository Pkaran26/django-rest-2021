from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    category = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

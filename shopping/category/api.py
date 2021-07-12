from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import CategorySerializer
from .models import Category

class CategoryCreateApi(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApi(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

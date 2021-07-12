from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product

class ProductCreateApi(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApi(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

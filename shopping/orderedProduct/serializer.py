from rest_framework import  serializers
from .models import OrderedProduct

class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = '__all__'

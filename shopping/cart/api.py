from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import CartSerializer
from .models import Cart

class CartCreateApi(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# class CartApi(generics.ListAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

class CartApi(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CartSerializer

    def get(self, request, *args,  **kwargs):
        data = Cart.objects.filter(customer=request.user)

        total = 0
        response = CartSerializer(data, context=self.get_serializer_context(), many=True).data
        # try:
        #     for d in response:
        #         print(d)
        #         total += (d.price * d.quantity)
        # except:
        #     print('e')


        return Response({
            "data": response,
            "total": total
        })

class CartUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDeleteApi(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

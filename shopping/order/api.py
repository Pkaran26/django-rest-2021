from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import OrderSerializer
from .models import Order

class OrderApi(generics.GenericAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = OrderSerializer

    def post(self, request, *args,  **kwargs):
        cartData = Cart.objects.filter(customer=request.user)

        response = {}
        #OrderSerializer(data, context=self.get_serializer_context(), many=True).data
        # try:
        #     for d in response:
        #         print(d)
        #         total += (d.price * d.quantity)
        # except:
        #     print('e')


        return Response({
            "data": response
        })

class OrderUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteApi(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

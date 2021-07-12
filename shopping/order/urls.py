from django.urls import path
from .api import OrderApi
#, OrderCreateApi, OrderUpdateApi, OrderDeleteApi

urlpatterns = [
    # path('api/create', OrderCreateApi.as_view()),
    path('api', OrderApi.as_view()),
    # path('api/<int:pk>', OrderUpdateApi.as_view()),
    # path('api/<int:pk>/delete', OrderDeleteApi.as_view()),
]

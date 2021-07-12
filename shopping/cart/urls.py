from django.urls import path
from .api import CartApi, CartCreateApi, CartUpdateApi, CartDeleteApi

urlpatterns = [
    path('api/create', CartCreateApi.as_view()),
    path('api', CartApi.as_view()),
    path('api/<int:pk>', CartUpdateApi.as_view()),
    path('api/<int:pk>/delete', CartDeleteApi.as_view()),
]

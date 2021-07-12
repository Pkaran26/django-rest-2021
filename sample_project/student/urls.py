from django.urls import path
from .api import StudentApi, StudentCreateApi, StudentUpdateApi, StudentDeleteApi

urlpatterns = [
    path('api/create',StudentCreateApi.as_view()),
    path('api',StudentApi.as_view()),
    path('api/<int:pk>',StudentUpdateApi.as_view()),
    path('api/<int:pk>/delete',StudentDeleteApi.as_view()),
]

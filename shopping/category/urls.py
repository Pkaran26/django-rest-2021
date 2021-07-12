from django.urls import path
from .api import CategoryApi, CategoryCreateApi, CategoryUpdateApi, CategoryDeleteApi

urlpatterns = [
    path('api/create', CategoryCreateApi.as_view()),
    path('api', CategoryApi.as_view()),
    path('api/<int:pk>', CategoryUpdateApi.as_view()),
    path('api/<int:pk>/delete', CategoryDeleteApi.as_view()),
]

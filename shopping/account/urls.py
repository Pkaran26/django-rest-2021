from django.urls import path, include
# from .api import SimpleApI
#
# urlpatterns = [
#     path('api/hello', SimpleApI.as_view() ),
# ]

from .api import RegisterApi
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
]

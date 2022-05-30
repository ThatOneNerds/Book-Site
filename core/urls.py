from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage),
    path('Books', browse),
    path('Discussion', discussion),
]

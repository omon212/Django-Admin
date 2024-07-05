from django.urls import path
from .views import *

urlpatterns = [
    path('update/', MyModelListUpdateView.as_view())
]




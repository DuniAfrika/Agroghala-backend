from django.urls import path
from .views import *

urlpatterns = [
    path('myghala/', MyGhalaListCreateView.as_view(), name='myghala-list'),
    path('mysoko/', MySokoListCreateView.as_view(), name='mysoko-list')
]
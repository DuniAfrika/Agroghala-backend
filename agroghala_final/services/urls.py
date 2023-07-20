from django.urls import path
from .views import *

urlpatterns = [
    path('ghala/', GhalaListCreateView.as_view(), name='ghala-list'),
    path('soko/', SokoListCreateView.as_view(), name='soko-list')
]
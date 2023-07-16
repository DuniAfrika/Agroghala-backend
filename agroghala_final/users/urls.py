from django.urls import path
from .views import *

urlpatterns = [
    #path('', NewUserView.as_view(), name='register-api'),
    path('', MyTokenObtainPairView.as_view(), name='token_obtain_pair')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('api/signup/', NewUserView.as_view(), name='register-api'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/csrf/', csrf_token_view, name='csrf_token_view'),
]
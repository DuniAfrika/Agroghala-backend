from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView
    )
from users.views import *
from STT.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('auth/', include('authentication.urls')),
    path('api-auth/drf/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/services/', include('services.urls')),
    path('api/myproducts/', include('myproducts.urls')),
    path('api/blogs/', include('blogs.urls')),
    path('process_voice_command/', AudioTranscriptionView.as_view(), name='process_voice_command'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

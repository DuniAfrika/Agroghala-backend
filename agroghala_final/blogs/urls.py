from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-api'),
    path('comments/', CommentListCreateView.as_view(), name='comment-api')
]
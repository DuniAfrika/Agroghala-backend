from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-api'),
    path('create-blog/', CreateBlogView.as_view(), name='create-blog'),
    path('comments/', CommentListCreateView.as_view(), name='comment-api'),
    path('blogs/<int:blog_id>/increase_views/', increase_blog_views, name='increase_blog_views'),
]

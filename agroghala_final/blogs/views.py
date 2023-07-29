from .models import *
from users.models import NewUser
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBlogView(APIView):
    """
    API endpoint to create a new blog.

    Methods: POST
    Authentication: SessionAuthentication (user must be logged in) and BasicAuthentication (user must provide credentials)
    Permissions: IsAuthenticated (user must be authenticated)

    Request Data:
    - title (string): The title of the blog.
    - content (string): The content of the blog.

    Response Data:
    - If successful, returns the serialized blog data with status code 201 Created.
    - If validation fails, returns the error messages with status code 400 Bad Request.
    """
    serializer_class = CreateBlogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handle POST requests to create a new blog.

        Parameters:
        - title (string): The title of the blog.
        - content (string): The content of the blog.

        Returns:
        - If successful, returns the serialized blog data with status code 201 Created.
        - If validation fails, returns the error messages with status code 400 Bad Request.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            content = serializer.data.get('content')
            author = request.user
            blog = Blog(title=title, content=content, author=author)
            blog.save()
            return Response(BlogSerializer(blog).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def increase_blog_views(request, blog_id):
    # Get the blog object or return 404 if not found
    blog = get_object_or_404(Blog, id=blog_id)

    # Increment the views count for the blog
    blog.views += 1
    blog.save()

    # Return a JSON response indicating success
    return JsonResponse({"message": "Views increased successfully."})


class CommentListCreateView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from .models import *
from users.models import NewUser

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'first_name', 'last_name', 'email')

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'content', 'views', 'date_posted')

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'content')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

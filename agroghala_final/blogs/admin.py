from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentsAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment
        fields = '__all__'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentsAdmin)

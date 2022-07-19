from django.contrib import admin

from .models import Post, BlogComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass
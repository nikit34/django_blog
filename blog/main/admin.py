from django.contrib import admin

from .models import Post, BlogComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tinyInject.js',)

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tinyInject.js',)
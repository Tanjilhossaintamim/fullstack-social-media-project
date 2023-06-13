from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('id', 'user', 'post_content',
                    'publish_at', 'update_at', 'post_image',)
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('id', 'user', 'post', 'comment', 'comment_date',)
    list_per_page = 10


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ('id', 'user', 'post',)
    list_per_page = 10


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    '''Admin View for Follow'''

    list_display = ('id', 'follower', 'following')
    list_per_page = 10

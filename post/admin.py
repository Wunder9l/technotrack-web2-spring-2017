from django.contrib import admin

from core.adminsupplier import CommentAndLikeAbleAdmin
from post.models import Post


@admin.register(Post)
class PostAdmin(CommentAndLikeAbleAdmin):
    readonly_fields = 'likes_count', 'comments_count'

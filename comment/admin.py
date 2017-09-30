from django.contrib import admin
from .models import Comment
from core.adminsupplier import LikeAbleAdmin


# Register your models here.
@admin.register(Comment)
class CommentAdmin(LikeAbleAdmin):
    readonly_fields = 'likes_count', 'edited_count'
    pass

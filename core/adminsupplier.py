from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from comment.adminsupplier import CommentsInline
from .models import Like


class LikesInline(GenericStackedInline):
    model = Like
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class LikeAbleAdmin(admin.ModelAdmin):
    inlines = LikesInline,


class CommentAndLikeAbleAdmin(admin.ModelAdmin):
    inlines = CommentsInline, LikesInline

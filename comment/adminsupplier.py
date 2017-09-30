from django.contrib.contenttypes.admin import GenericTabularInline

from comment.models import Comment


class CommentsInline(GenericTabularInline):
    model = Comment
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    readonly_fields = 'likes_count', 'edited_count'

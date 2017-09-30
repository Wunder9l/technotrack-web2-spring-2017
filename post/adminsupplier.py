from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Post


# class PostsInLine(GenericStackedInline):
#     model = Post
#     ct_field = 'content_type'
#     ct_fk_field = 'object_id'
#     readonly_fields = 'likes_count', 'comments_count'

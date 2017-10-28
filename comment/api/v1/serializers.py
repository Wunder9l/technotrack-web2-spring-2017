from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comment.models import Comment
from core.serializers import UserBriefSerializer, LikeAbleObjectSerializer
from core.utils import get_class_as_string


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id', 'author', 'object_id', "content_type", 'text', 'updated',  # 'created',
        read_only_fields = 'author', 'id', 'updated',  # 'created',

    def get_content_type_as_string(self, object):
        return get_class_as_string(object.object)

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comment.models import Comment
from core.serializers import UserBriefSerializer, LikeAbleObjectSerializer
from core.utils import get_class_as_string


class CommentSerializer(ModelSerializer):
    author = UserBriefSerializer(read_only=True, required=False)
    object = LikeAbleObjectSerializer(read_only=True, required=False)
    content_type_as_string = serializers.SerializerMethodField(read_only=True)
    content_type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all(), many=False)

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = 'id', 'author', 'object', 'object_id', "content_type", 'content_type_as_string', 'text', 'created', 'updated',
        read_only_fields = 'author', 'id', 'object', 'created', 'updated', 'content_type_as_string',

    def get_content_type_as_string(self, object):
        return get_class_as_string(object.object)

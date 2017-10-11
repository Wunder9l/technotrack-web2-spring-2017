from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    author_username = serializers.ReadOnlyField(source='author.username')
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ("id",
                            "author",
                            "author_username",
                            "likes",
                            "created",
                            "updated",
                            "likes_count",
                            "comments_count",)

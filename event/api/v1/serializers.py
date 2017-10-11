from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from event.models import Event


class EventSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    # likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        # read_only_fields = ("id",
        #                     "author",
        #                     "author_username",
        #                     "likes",
        #                     "created",
        #                     "updated",
        #                     "likes_count",
        #                     "comments_count",)

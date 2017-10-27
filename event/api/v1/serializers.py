from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.serializers import UserBriefSerializer
from event.models import Event


class EventSerializer(ModelSerializer):
    user = UserBriefSerializer()

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ("id", "user", "created", "updated",)
        #                     "author",
        #                     "author_username",
        #                     "likes",
        #                     "likes_count",
        #                     "comments_count",)

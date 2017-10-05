from rest_framework import serializers

from core.models import Like, User
from core.serializers import ModelWithAuthorSerializer


class LikeSerializer(ModelWithAuthorSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

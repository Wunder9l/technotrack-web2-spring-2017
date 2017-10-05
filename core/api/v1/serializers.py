from rest_framework import serializers

from core.models import Like, User
from core.serializers import ModelWithAuthorSerializer


class LikeSerializer(ModelWithAuthorSerializer):
    object = serializers.ReadOnlyField(source='object.get_title_for_like')
    content_type = serializers.SerializerMethodField(read_only=True)

    def get_content_type(self, like_object):
        type_str = str(like_object.object.__class__)
        return type_str[type_str.find("'") + 1:type_str.rfind("'")]

    class Meta:
        model = Like
        fields = 'author', 'created', 'updated', 'object', 'content_type'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

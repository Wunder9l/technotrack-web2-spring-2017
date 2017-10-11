from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Like, User
from core.serializers import ModelWithAuthorSerializer


class LikeSerializer(ModelSerializer):
    object = serializers.ReadOnlyField(source='object.get_title_for_like', read_only=True)
    # object_id = serializers.IntegerField(source='object_id', read_only=False)
    content_type_as_string = serializers.SerializerMethodField(read_only=True)
    content_type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all(), many=False)
    author = serializers.ReadOnlyField(source='author.id')
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Like
        fields = '__all__'
        # fields = 'author', 'object', 'object_id', "content_type", 'content_type_as_string', 'created', 'updated',
        read_only_fields = 'author', 'author_username', 'object', 'id', 'created', 'updated', 'content_type_as_string',

    def get_content_type_as_string(self, like_object):
        type_str = str(like_object.object.__class__)
        return type_str[type_str.find("'") + 1:type_str.rfind("'")]
        #

    def save(self, **kwargs):
        super(LikeSerializer, self).save(**kwargs)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'id'


class UserDetailSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='object.username', read_only=True)
    # first_name = serializers.ReadOnlyField(source='object.first_name', read_only=True)
    # last_name = serializers.ReadOnlyField(source='object.last_name', read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "last_login", "is_superuser",
                  "is_active", "date_joined", "objects_count", "groups", "relationships",)
        read_only_fields = ("username", "id", "data_joined", "objects_count", "relationships",
                            "last_login", "is_superuser", "is_active")

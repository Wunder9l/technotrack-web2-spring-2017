from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Like, User, RelationshipEnum, Relationship, RELATIONSHIP_BLOCKED
from core.serializers import UserBriefSerializer, LikeAbleObjectSerializer
from core.utils import check_password_to_satisfy_requirements


class LikeSerializer(ModelSerializer):
    object = LikeAbleObjectSerializer(read_only=True, required=False)
    content_type_as_string = serializers.SerializerMethodField(read_only=True)
    content_type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all(), many=False)
    author = UserBriefSerializer(read_only=True, required=False)

    class Meta:
        model = Like
        # fields = '__all__'
        fields = 'id', 'author', 'object', 'object_id', "content_type", 'content_type_as_string', 'created', 'updated',
        read_only_fields = 'author', 'object', 'id', 'created', 'updated', 'content_type_as_string',

    def get_content_type_as_string(self, like_object):
        type_str = str(like_object.object.__class__)
        return type_str[type_str.find("'") + 1:type_str.rfind("'")]
        #


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50, required=True)
    new_password = serializers.CharField(max_length=50, required=True)

    def validate(self, data):
        if data['old_password']:
            new_password_check_errors = check_password_to_satisfy_requirements(data['new_password'])
            if new_password_check_errors:
                raise serializers.ValidationError("Error on new_password: " + new_password_check_errors)
            else:
                return data
        else:
            raise serializers.ValidationError("Error on old_password: Field cannot be empty")


class CreateRelationshipSerializer(serializers.Serializer):
    to_person = serializers.IntegerField(required=True)
    status = serializers.IntegerField(required=True)

    def validate(self, data):
        data = super(CreateRelationshipSerializer, self).validate(data)
        if RelationshipEnum().get_name(data['status']):
            if len(User.objects.filter(id=data['to_person'])) > 0:
                return data
            else:
                raise serializers.ValidationError("User with id (%d) not found" % data['to_person'])
        else:
            raise serializers.ValidationError("Invalid status field")


class UserSelfSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    blocked = serializers.SerializerMethodField()

    def get_following(self, obj):
        return [{'id': u.id, 'username': u.username} for u in obj.get_following()]

    def get_blocked(self, obj):
        return [{'id': u.id, 'username': u.username} for u in
                obj.get_relationships(RelationshipEnum().get_id(RELATIONSHIP_BLOCKED))]

    def update(self, instance, validated_data):
        if validated_data and instance:
            if 'avatar' in validated_data:
                instance.avatar = validated_data['avatar']
                instance.save()
                del validated_data['avatar']
                if not validated_data:
                    return instance
            User.objects.filter(id=instance.id).update(**validated_data)
            instance.refresh_from_db()
        return instance

    class Meta:
        model = User
        read_only_fields = 'last_login', 'date_joined', 'objects_count', 'user_permissions', \
                           'is_active', 'is_staff', 'is_superuser'
        exclude = 'password', 'relationships'
        # extra_kwargs = {'password': {'write_only': True}}


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

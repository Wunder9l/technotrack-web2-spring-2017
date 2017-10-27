from rest_framework import serializers

from core.models import User, LikeAbleNotAbstract


class UserBriefSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(read_only=True, slug_field='username',)
    # author_url = serializers.HyperlinkedIdentityField(view_name='id')


    class Meta:
        model = User
        fields = 'id', 'username'
        read_only_fields = 'id', 'username'


class LikeAbleObjectSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='get_title_for_like', read_only=True)

    class Meta:
        model = LikeAbleNotAbstract
        fields = 'id', 'title'
        read_only_fields = 'id', 'title'

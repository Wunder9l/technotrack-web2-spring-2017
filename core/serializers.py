from rest_framework import serializers


class ModelWithAuthorSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username',)

    # author_url = serializers.HyperlinkedIdentityField(view_name='id')
    class Meta:
        abstract = True


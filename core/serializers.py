from rest_framework import serializers


class ModelWithAuthorSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        abstract = True

from rest_framework import serializers

from app.models import New, Tag


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'description', 'tag', 'creator', 'date_of_creation']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

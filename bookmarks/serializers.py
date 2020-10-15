from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ("title", "url")


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
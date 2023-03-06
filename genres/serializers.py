from rest_framework import serializers
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    class Meta:
        model = Genre
        fields = "__all__"
        read_only_fields = ["id"]

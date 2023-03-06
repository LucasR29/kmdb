from genres.serializers import GenreSerializer
from rest_framework import serializers
from genres.models import Genre
from datetime import timedelta
from datetime import datetime
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "duration", "budget", "overview", "genres", "premiere"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        genres = validated_data.pop("genres")
        duration = validated_data.pop("duration")

        hours = datetime.strptime(duration, "%H:%M:%S").time().hour
        minutes = datetime.strptime(duration, "%H:%M:%S").time().minute
        seconds = datetime.strptime(duration, "%H:%M:%S").time().second

        duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        genre_objects = []

        for i in genres:
            genre = Genre.objects.filter(name__icontains=i["name"]).first()

            if not genre:
                genre = Genre.objects.create(**i)

            genre_objects.append(genre)

        movie = Movie.objects.create(**validated_data, duration=duration)
        movie.genres.set(genre_objects)
        movie.save()

        return movie

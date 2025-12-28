from rest_framework import serializers

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "name",
        )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "first_name",
            "last_name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "name",
            "rows",
            "seats_in_row",
        )


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True
    )
    actors = ActorSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "show_time",
            "movie",
            "cinema_hall"
        )

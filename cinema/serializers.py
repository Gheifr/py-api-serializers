from rest_framework import serializers

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "name",
        )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "full_name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
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
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = (
            "id",
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
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )

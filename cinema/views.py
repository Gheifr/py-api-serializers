from rest_framework import viewsets

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import (
    GenreSerializer, GenreListSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer, ActorListSerializer, MovieListSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        elif self.action == "retrieve":
            return GenreSerializer

        return self.serializer_class


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorSerializer
        return self.serializer_class


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = (Movie.objects.all()
                .prefetch_related("actors")
                .prefetch_related("genres"))
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return self.serializer_class


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

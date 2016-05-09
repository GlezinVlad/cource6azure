import django_filters
from rest_framework import generics
from rest_framework import filters

from serializers import MovieSerializer
from models import Movie


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_fields = ('title',)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

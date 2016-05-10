import django_filters
from rest_framework import generics
from rest_framework import filters

from serializers import MovieSerializer
from models import Movie


class MovieListView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        title_filter = self.request.query_params.get('title')
        if title_filter:
            a = Movie.objects.filter(title__icontains=title_filter)
            return a
        else:
            return Movie.objects.all()


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

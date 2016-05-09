import django_filters
from rest_framework import generics
from rest_framework import filters

from models import Seance
from serializers import SeanceSerializer


class SeanceFilter(filters.FilterSet):
    starts_after = django_filters.IsoDateTimeFilter(name="starts_at", lookup_type='gte')
    starts_before = django_filters.IsoDateTimeFilter(name="starts_at", lookup_type='lte')

    class Meta:
        model = Seance
        fields = ['starts_before', 'starts_after']


class SeanceByMovieListView(generics.ListCreateAPIView):
    serializer_class = SeanceSerializer
    filter_class = SeanceFilter

    def get_queryset(self):
        seance_id = self.kwargs['movie_id']
        return Seance.objects.filter(movie_id=seance_id)


class SeanceListView(generics.ListCreateAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    filter_class = SeanceFilter


class SeanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer

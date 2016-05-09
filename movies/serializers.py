from rest_framework import serializers
from models import Movie
from seances.models import Seance


class MovieSerializer(serializers.ModelSerializer):
    seances = serializers.PrimaryKeyRelatedField(many=True, queryset=Seance.objects.all(), allow_null=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'about', 'image_url', 'seances')

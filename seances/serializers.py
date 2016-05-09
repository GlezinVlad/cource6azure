from rest_framework import serializers

from models import Seance
from tickets.models import Ticket


class SeanceSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all(), allow_null=True)

    class Meta:
        model = Seance
        fields = ('id', 'movie', 'starts_at', 'duration', 'tickets')

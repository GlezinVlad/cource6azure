from rest_framework import generics


from models import Ticket
from serializers import TicketSerializer


class TicketBySeanceListView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    filter_fields = ('user_email',)

    def get_queryset(self):
        seance_id = self.kwargs['seance_id']
        return Ticket.objects.filter(seance_id=seance_id)


class TicketListView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    filter_fields = ('user_email',)

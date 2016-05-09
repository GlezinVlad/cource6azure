from __future__ import unicode_literals

from django.db import models

from seances.models import Seance


class Ticket(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, related_name='tickets')
    row = models.IntegerField()
    place = models.IntegerField()
    user_id = models.IntegerField()

    def __unicode__(self):
        return 'Ticket(seance: {0}, row: {1}, place: {2})'.format(self.seance, self.row, self.place)

    class Meta:
        unique_together = ('row', 'place', 'seance')

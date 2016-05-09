from __future__ import unicode_literals

from django.db import models

from movies.models import Movie


class Seance(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seances')
    starts_at = models.DateTimeField()
    duration = models.IntegerField()

    def __unicode__(self):
        return 'Seance(movie title: {0}, starts at: {1})'.format(self.movie.title, self.starts_at)

from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    image_url = models.URLField()

    def __unicode__(self):
        return 'Movie(title: {0})'.format(self.title)

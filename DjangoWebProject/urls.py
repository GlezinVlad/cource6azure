"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import url, include

urlpatterns = [
    url(r'^movies/', include('movies.urls')),
    url(r'^seances/', include('seances.urls')),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^reports/', include('reports.urls')),
]


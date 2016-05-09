from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.MovieDetailView.as_view()),
    url(r'^$', views.MovieListView.as_view()),
]
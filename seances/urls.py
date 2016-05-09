from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.SeanceDetailView.as_view()),
    url(r'^$', views.SeanceListView.as_view()),
    url(r'^bymovie/(?P<movie_id>[0-9]+)/$', views.SeanceByMovieListView.as_view()),
]
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<seance_id>[0-9]+)/$', views.TicketListView.as_view()),
    url(r'^$', views.index_view),
]
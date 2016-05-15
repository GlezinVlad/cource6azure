import views
from django.conf.urls import url

urlpatterns = [
    url(r'^salesbyrow/$', views.sales_by_row_report),
    url(r'^earnings/$', views.earnings_report),
    url(r'^movie_earnings/$', views.movie_earnings_report),
]
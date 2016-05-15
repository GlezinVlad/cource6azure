'^movies/(?P<pk>[0-9]+)/$', MovieDetailView

'^movies/$', MovieListView                                                  filters: title

'seances/^(?P<pk>[0-9]+)/$' - SeanceDetailView

'seances/^$' - SeanceListView                                               filters: starts_before, starts_after  (dates)

'seances/^bymovie/(?P<movie_id>[0-9]+)/$' - SeanceByMovieListView           filters: starts_before, starts_after  (dates)


'^tickets/(?P<seance_id>[0-9]+)/$' - TicketBySeanceListView                 filters: user_email

'^tickets/$' - TicketListView                                               filters: user_email


'^reports/salesbyrow/$' - sales_by_row_report                               filters: max_date, min_date  (dates), movie_id

'^reports/earnings/$' - earnings_report                                     filters: max_date, min_date  (dates)

'^reports/movie_earnings/$' - movie_earnings_report                         movie_id - required param


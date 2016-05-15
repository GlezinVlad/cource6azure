from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.db.models import Count, Sum, F

from seances.models import Seance
from tickets.models import Ticket
from DjangoWebProject.appconfigurations import ROWS, PLACES


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def sales_by_row_report(request):
    q = Ticket.objects

    if request.GET.get('movie_id', ''):
        q = q.filter(seance__movie_id=request.GET['movie_id'])

    if request.GET.get('max_date', ''):
        q = q.filter(seance__starts_at__lte=request.GET['max_date'])

    if request.GET.get('min_date', ''):
        q = q.filter(seance__starts_at__gte=request.GET['min_date'])

    res = {}

    for row in range(1, ROWS+1):
        res[row] = q.filter(row=row).count()                                # TODO: Write SQL
    return Response(res, content_type=None)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def earnings_report(request):
    q = Seance.objects.select_related('movie')

    if request.GET.get('max_date', ''):
        q = q.filter(starts_at__lte=request.GET['max_date'])

    if request.GET.get('min_date', ''):
        q = q.filter(starts_at__gte=request.GET['min_date'])

    seances = q.annotate(tickets_sold=Count('tickets')).annotate(earnings=F('tickets_sold')*F('price'))

    res = {
        'earnings': 0,
        'max_earnings': 0,          # with all tickets sold
        'earnings_by_movie': {},
    }

    for seance in seances:
        res['earnings'] += seance.earnings
        res['max_earnings'] += seance.price * ROWS * PLACES
        if seance.movie.title in res['earnings_by_movie']:
            res['earnings_by_movie'][seance.movie.title] += seance.earnings
        else:
            res['earnings_by_movie'][seance.movie.title] = seance.earnings

    return Response(res)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def movie_earnings_report(request):
    q = Seance.objects.filter(movie_id=request.GET['movie_id']).select_related('movie')
    seances = q.annotate(tickets_sold=Count('tickets')).annotate(earnings=F('tickets_sold') * F('price'))

    if not q:
        return Response({'detail': 'no seances for this movie'})

    res = {
        'movie_title': seances[0].movie.title,
        'earnings': 0,
        'max_earnings': 0,
        'earnings_by_seance': {},
    }
    for seance in seances:
        res['earnings'] += seance.earnings
        res['max_earnings'] += seance.price * ROWS * PLACES
        res['earnings_by_seance'][str(seance.starts_at)] = seance.earnings

    return Response(res)

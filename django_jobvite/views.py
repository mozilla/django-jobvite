from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404

from django_jobvite.models import Position
from django_jobvite.serializers import serialize


def _cleanse_params(params):
    """
    Convert a ``QueryDict`` into a dictionary of parameters ready
    for a call to ``filter``. Remove any keys that are not fields
    to prevent a ``FieldError``. Also exclude primary keys.
    """
    cleansed = {}
    field_names = [field.name for field in Position._meta.fields
                   if not field.primary_key]
    for k, v in params.iteritems():
        if k in field_names:
            cleansed[k + '__contains'] = v
    return cleansed


def position(request, job_id):
    position = get_object_or_404(Position, job_id=job_id)
    return HttpResponse(serialize((position,)),
                        content_type='application/json')


def positions(request):
    if len(request.GET.keys()):
        params = _cleanse_params(request.GET)
        positions = Position.objects.filter(**params)
    else:
        positions = Position.objects.all()
    if not positions:
        return HttpResponseNotFound()
    return HttpResponse(serialize(positions), content_type='application/json')

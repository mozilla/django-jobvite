from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404

from django_jobvite.models import Position, Category
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
            cleansed[k + '__icontains'] = v
    return cleansed


def positions(request, job_id=None):
    if job_id:
        position = get_object_or_404(Position, job_id=job_id)
        return HttpResponse(serialize((position,)),
                            content_type='application/json')
    params = _cleanse_params(request.GET)
    positions = Position.objects.filter(**params)
    if not positions:
        return HttpResponseNotFound()
    return HttpResponse(serialize(positions), content_type='application/json')


def categories(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        positions = category.position_set.all()
        return HttpResponse(serialize(positions),
                            content_type='application/json')
    params = _cleanse_params(request.GET)
    categories = Category.objects.filter(**params)
    if not categories:
        return HttpResponseNotFound()
    return HttpResponse(serialize(categories), content_type='application/json')

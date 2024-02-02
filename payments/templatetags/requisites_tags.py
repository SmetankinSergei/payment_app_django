from django import template
from django.db.models import Q

from payments.models import Requisite

register = template.Library()


@register.simple_tag()
def get_requisites(feature=None):
    if feature:
        return Requisite.objects.order_by(feature)
    return Requisite.objects.all()


@register.simple_tag()
def get_search_result(query):
    if query.isdigit():
        result = Requisite.objects.filter(limit__lte=int(query))
    else:
        result = Requisite.objects.filter(
            Q(payment_type__icontains=query) |
            Q(source_type__icontains=query) |
            Q(full_name__icontains=query) |
            Q(phone__icontains=query)
        )
    return result

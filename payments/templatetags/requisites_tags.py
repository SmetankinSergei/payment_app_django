from django import template

from payments.models import Requisite

register = template.Library()


@register.simple_tag()
def get_requisites(feature=None):
    if feature:
        return Requisite.objects.order_by(feature)
    return Requisite.objects.all()

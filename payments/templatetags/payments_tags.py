from django import template
from django.db.models import Q

from payments.models import Requisite, Payment

register = template.Library()


@register.simple_tag()
def get_payments():
    return Payment.objects.all()

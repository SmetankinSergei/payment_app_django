from django import template

from payments.models import Payment

register = template.Library()


@register.simple_tag()
def get_payments():
    return Payment.objects.all()

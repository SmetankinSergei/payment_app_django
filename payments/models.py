from enum import Enum

from django.db import models


class PaymentStatus(Enum):
    AWAITING = 'awaiting'
    CANCELED = 'canceled'
    PAID = 'paid'


class Payment(models.Model):
    amount = models.PositiveIntegerField()
    requisites = models.ForeignKey(to='Requisites', on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=[(status.value, status.name) for status in PaymentStatus])


class PaymentType(Enum):
    CARD = 'card'
    ACCOUNT = 'account'


class SourceType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'


class Requisites(models.Model):
    payment_type = models.CharField(max_length=10,
                                    choices=[(payment_type.value, payment_type.name) for payment_type in PaymentType])

    source_type = models.CharField(max_length=10,
                                   choices=[(source_type.value, source_type.name) for source_type in SourceType])
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    limit = models.PositiveIntegerField()

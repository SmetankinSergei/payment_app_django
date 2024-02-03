from rest_framework import serializers
from .models import Requisite


class RequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = ('id', 'payment_type', 'source_type', 'full_name', 'phone', 'limit')

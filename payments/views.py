from django.contrib.auth.decorators import login_required
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment, Requisite, PaymentStatus

from payments.templatetags.payments_tags import get_payments
from payments.templatetags.requisites_tags import get_requisites, get_search_result

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .serializers import RequisiteSerializer


def show_payments(request):
    payments_list = get_payments()
    requisites_list = get_requisites()

    payments_page = request.GET.get('payments_page', 1)
    requisites_page = request.GET.get('requisites_page', 1)
    items_per_page = 30

    paginator_payments = Paginator(payments_list, items_per_page)
    paginator_requisites = Paginator(requisites_list, items_per_page)

    try:
        payments = paginator_payments.page(payments_page)
    except PageNotAnInteger:
        payments = paginator_payments.page(1)
    except EmptyPage:
        payments = paginator_payments.page(paginator_payments.num_pages)

    try:
        requisites = paginator_requisites.page(requisites_page)
    except PageNotAnInteger:
        requisites = paginator_requisites.page(1)
    except EmptyPage:
        requisites = paginator_requisites.page(paginator_requisites.num_pages)

    context = {
        'title': 'payments',
        'payments': payments,
        'requisites': requisites,
    }
    return render(request, 'payments/start_page.html', context)


@login_required
def show_requisites(request):
    query = request.GET.get('query')
    requisites = get_requisites(request.GET.get('feature'))

    if query:
        requisites = get_search_result(query)

    context = {
        'title': 'requisites',
        'requisites': requisites,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'payments/requisites_list.html', context)
    else:
        return render(request, 'payments/show_requisites.html', context)



@swagger_auto_schema(
    method='get',
    responses={200: 'OK', 404: 'Not Found'},
    operation_summary="Get invoice status",
    operation_description="Getting payment status by its id."
)
@api_view(['GET'])
def get_invoice_status(request, invoice_id):
    payment = get_object_or_404(Payment, id=invoice_id)
    return Response({'status': payment.status})


@swagger_auto_schema(
    method='get',
    responses={200: 'OK', 404: 'Not Found'},
    operation_summary="Create invoice by requisite id and payment amount",
    operation_description="Create invoice by requisite id and payment amount."
)
@api_view(['GET'])
def create_invoice(request, requisite_id, amount):
    requisite = get_object_or_404(Requisite, pk=requisite_id)
    print(requisite)
    payment = Payment.objects.create(
        amount=amount,
        requisites=requisite,
        status=PaymentStatus.AWAITING.value
    )
    requisite_serializer = RequisiteSerializer(requisite)
    return Response({'id': payment.id, 'requisite': requisite_serializer.data})

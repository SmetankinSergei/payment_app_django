from django.contrib.auth.decorators import login_required

from payments.templatetags.payments_tags import get_payments
from payments.templatetags.requisites_tags import get_requisites, get_search_result

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


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
    if query:
        requisites = get_search_result(query)
    else:
        requisites = get_requisites(request.GET.get('feature'))
    context = {
        'title': 'requisites',
        'requisites': requisites,
    }
    return render(request, 'payments/show_requisites.html', context)

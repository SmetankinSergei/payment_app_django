from django.shortcuts import render

from payments.templatetags.requisites_tags import get_requisites, get_search_result


def start_page(request):
    return render(request, 'payments/start_page.html', {'title': 'start page'})


def show_payments(request):
    return render(request, 'payments/start_page.html', {'title': 'payments'})


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

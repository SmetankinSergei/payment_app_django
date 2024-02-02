from django.shortcuts import render

from payments.templatetags.requisites_tags import get_requisites


def start_page(request):
    return render(request, 'payments/start_page.html', {'title': 'start page'})


def show_payments(request):
    return render(request, 'payments/start_page.html', {'title': 'payments'})


def show_requisites(request):
    if request.GET.get('feature'):
        requisites = get_requisites(request.GET.get('feature'))
    else:
        requisites = get_requisites()
    context = {
        'title': 'requisites',
        'requisites': requisites,
    }
    return render(request, 'payments/show_requisites.html', context)

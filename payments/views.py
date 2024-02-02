from django.shortcuts import render


def start_page(request):
    return render(request, 'payments/start_page.html')


def show_payments(request):
    return render(request, 'payments/start_page.html')


def show_requisites(request):
    return render(request, 'payments/show_requisites.html')

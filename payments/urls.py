from django.urls import path

from payments import views

app_name = 'payments'

urlpatterns = [
    path('', views.show_payments, name='show_payments'),
    path('show_requisites/', views.show_requisites, name='show_requisites'),
    path('api/create_invoice/<int:requisite_id>/<int:amount>', views.create_invoice, name='create_invoice'),
    path('api/get_invoice_status/<int:invoice_id>/', views.get_invoice_status, name='get_invoice_status'),
]

from django.urls import path

from payments import views

app_name = 'payments'

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('show_payments/', views.show_payments, name='show_payments'),
    path('show_requisites/', views.show_requisites, name='show_requisites'),
]

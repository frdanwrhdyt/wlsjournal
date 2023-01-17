from django.urls import path
from .views import *

urlpatterns = [
    path('user-business', UserBusinessView.as_view()),
    path('selling-product', SellingProductView.as_view()),
    path('customer', CustomerView.as_view()),
    path('invoice', InvoiceView.as_view()),
    path('payment-type', PaymentTypeView.as_view()),
    path('order', OrderView.as_view()),
    path('order/<int:id>', OrderDetailView.as_view()),
]
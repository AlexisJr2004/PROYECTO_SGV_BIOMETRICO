from django.urls import path
from app.sales.views import invoice

app_name='sale'
urlpatterns = [    
    path('invoice_list/', invoice.InvoiceListView.as_view(),name='invoice_list'),
    path('invoice_create/', invoice.InvoiceCreateView.as_view(),name='invoice_create'),
    path('invoice_update/<int:pk>/', invoice.InvoiceUpdateView.as_view(),name='invoice_update'),
    path('invoice_delete/<int:pk>/', invoice.InvoiceDeleteView.as_view(),name='invoice_delete'),
    
]

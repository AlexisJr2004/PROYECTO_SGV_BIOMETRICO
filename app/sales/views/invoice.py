from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.sales.forms.invoice import InvoiceForm, InvoiceDetailFormSet
from app.sales.models import Invoice
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin

class InvoiceListView(PermissionMixin,ListViewMixin, ListView):
    template_name = 'sale/invoices/list.html'
    model = Invoice
    context_object_name = 'invoices'
    permission_required = 'view_invoice'
    
    # def get_queryset(self):
    #     q1 = self.request.GET.get('q') # ver
    #     if q1 is not None: 
    #         self.query.add(Q(name__icontains=q1), Q.OR) 
    #     return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['permission_add'] = context['permissions'].get('add_supplier','')
        context['create_url'] = reverse_lazy('sale:invoice_create')
        return context

from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.sales.forms.invoice import InvoiceForm, InvoiceDetailFormSet
from app.sales.models import Invoice
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin

class InvoiceCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Invoice
    template_name = 'sale/invoices/form.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('sale:invoice_list')
    permission_required = 'add_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detail_formset'] = InvoiceDetailFormSet(self.request.POST)
        else:
            context['detail_formset'] = InvoiceDetailFormSet()
        context['grabar'] = 'Grabar Ventas'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detail_formset = context['detail_formset']
        if form.is_valid() and detail_formset.is_valid():
            self.object = form.save()
            detail_formset.instance = self.object
            detail_formset.save()
            messages.success(self.request, f"Éxito al crear la venta {self.object.id}.")
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class InvoiceUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Invoice
    template_name = 'sale/invoices/form.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('sale:invoice_list')
    permission_required = 'change_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detail_formset'] = InvoiceDetailFormSet(self.request.POST, instance=self.object)
        else:
            context['detail_formset'] = InvoiceDetailFormSet(instance=self.object)
        context['grabar'] = 'Actualizar Compañías'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detail_formset = context['detail_formset']
        if form.is_valid() and detail_formset.is_valid():
            self.object = form.save()
            detail_formset.instance = self.object
            detail_formset.save()
            messages.success(self.request, f"Éxito al actualizar la venta {self.object.id}.")
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
class InvoiceDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Invoice
    template_name = 'sale/delete.html'
    success_url = reverse_lazy('sale:invoice_list')
    permission_required = 'delete_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Ventas'
        context['id'] = f"¿Desea Eliminar la Venta? {self.object.id}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la venta {self.object.id}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    

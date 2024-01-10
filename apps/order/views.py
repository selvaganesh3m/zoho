from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .models import SalesOrder, ProductionOrder
from .forms import SalesOrderForm, ProductionOrderForm, SalesOrderInvoiceForm
from django.http import Http404
from .utils import send_email_to_user, generate_and_save_invoice
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



class ShowSalesOrdersView(View):
    template_name = 'order/show-sales-orders.html'

    def get(self, request, *args, **kwargs):
        sales_orders = SalesOrder.objects.all()
        return render(request, self.template_name, {"sales_orders": sales_orders})
    

class AddSalesOrderView(View):
    form_class = SalesOrderForm
    initial = {"key": "value"}
    template_name = 'order/add-sales-order.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('order:show-sales-orders'))
        return render(request, self.template_name, {"form": form})
    

class ShowProductionOrdersView(View):
    template_name = 'order/show-production-orders.html'

    def get(self, request, *args, **kwargs):
        production_orders = ProductionOrder.objects.all()
        return render(request, self.template_name, {"production_orders": production_orders})
    

class AddProductionOrderView(View):
    form_class = ProductionOrderForm
    initial = {"key": "value"}
    template_name = 'order/add-production-order.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('order:show-production-orders'))
        return render(request, self.template_name, {"form": form})
    
class CompleteProductionOrderView(View):
    template_name = 'order/show-production-orders.html'

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        try:
            order = ProductionOrder.objects.get(id=order_id)
        except ProductionOrder.DoesNotExist:
            raise Http404("Purchase Order does not exist")
        send_email_to_user(order)
        generate_and_save_invoice(order)
        order.is_completed = True
        order.save(update_fields=['is_completed'])
        return redirect(reverse('order:show-production-orders'))
    

class GenerateSalesOrderInvoiceView(View):
    form_class = SalesOrderInvoiceForm
    initial = {"key": "value"}
    template_name = 'order/generate-sales-order-invoice.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('order:show-sales-orders'))
        return render(request, self.template_name, {"form": form})
        
        

        



from typing import Any
from django import forms
from apps.product.models import Product
from apps.warehouse.models import WarehouseStock
from .models import SalesOrder, ProductionOrder
from .utils import generate_and_save_invoice




class SalesOrderForm(forms.Form):
    ORDER_STATUS_CHOICES = (
        ("ORDER_RECIEVED","ORDER RECIEVED"),
        ("ORDER_PROCESSING", "ORDER PROCESSING"),
        ("ORDER_COMPLETED", "ORDER_COMPLETED"),
        ("INVOICE_ISSUED", "INVOICE ISSUED"),
    )
    cutomer_name = forms.CharField(max_length=175)
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Choose Products"
    )
    status = forms.ChoiceField(choices=ORDER_STATUS_CHOICES, label='Status', initial='ORDER_RECIEVED')


    def save(self):
        products = self.cleaned_data['products']
        name = self.cleaned_data['cutomer_name']
        sales_order_products = []
        production_order_products = []
        for product in products:
            if WarehouseStock.objects.filter(product=product).exists():
                sales_order_products.append(product)
                sales_orders = SalesOrder.objects.create(customer=name)
                sales_orders.products.set(sales_order_products)
            else:
                production_order_products.append(product)
                production_orders = ProductionOrder.objects.create(customer=name, is_from_sales_order=True)
                production_orders.products.set(production_order_products)
        


class ProductionOrderForm(forms.ModelForm):
    class Meta:
        model = ProductionOrder
        exclude = ('is_from_sales_order', 'is_completed', 'invoice')


# Invoice Forms        
class SalesOrderInvoiceForm(forms.Form):
    order_id = forms.IntegerField()

    def clean_order_id(self):
        order_id = self.cleaned_data['order_id']
        try:
            order = SalesOrder.objects.get(id=order_id)
        except SalesOrder.DoesNotExist:
            raise forms.ValidationError('Order ID invalid')
        if order.status != "ORDER_COMPLETED":
            raise forms.ValidationError('Invoice can be generated only for completed order')
        return order_id

    def save(self):
        order_id = self.cleaned_data['order_id']
        try:
           order = SalesOrder.objects.get(id=order_id)
        except SalesOrder.DoesNotExist:
            return None
        if not order.invoice:
            generate_and_save_invoice(order)
        order.status = "INVOICE_ISSUED"
        order.save()

        
        













        

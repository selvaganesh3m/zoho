
from django import forms
from apps.warehouse.models import Warehouse, WarehouseStock
from apps.product.models import Product


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'


class AddWarehouseStockForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select Product')
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), empty_label='Select Warehouse')
    quantity = forms.IntegerField()

    class Meta:
        model = WarehouseStock
        fields = '__all__'
    
    def save(self, commit=True):
        product = self.cleaned_data['product']
        warehouse = self.cleaned_data['warehouse']
        quantity = self.cleaned_data['quantity']

        # Check if the product already exists in the warehouse
        existing_stock = WarehouseStock.objects.filter(product=product, warehouse=warehouse).first()

        if existing_stock:
            # If it exists, update the quantity
            existing_stock.quantity += quantity
            instance = existing_stock
        else:
            # If it doesn't exist, create a new WarehouseStock instance
            instance = super().save(commit=False)
            instance.quantity = quantity

        if commit:
            instance.save()

        return instance
        


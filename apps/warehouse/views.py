from django.shortcuts import render
from .forms import WarehouseForm, AddWarehouseStockForm
from django.views import View
from django.http import HttpResponseRedirect
from .models import Warehouse, WarehouseStock
from django.shortcuts import redirect
from django.urls import reverse



class ShowWarehouseView(View):
    template_name = 'warehouse/show-warehouse.html'

    def get(self, request, *args, **kwargs):
        warehouses = Warehouse.objects.all()
        return render(request, self.template_name, {"warehouses": warehouses})
    

class AddWarehouseView(View):
    form_class = WarehouseForm
    initial = {"key": "value"}
    template_name = 'warehouse/add-warehouse.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('warehouse:show-warehouses'))
        return render(request, self.template_name, {"form": form})
    

class ShowWarehouseStockView(View):
    template_name = 'warehouse/show-warehouse-stocks.html'

    def get(self, request, *args, **kwargs):
        warehouse_stocks = WarehouseStock.objects.all()
        return render(request, self.template_name, {"warehouse_stocks": warehouse_stocks})



class AddWarehouseStockView(View):
    form_class = AddWarehouseStockForm
    initial = {"key": "value"}
    template_name = 'warehouse/add-stock.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('warehouse:show-warehouses')) # Dummy
        return render(request, self.template_name, {"form": form})


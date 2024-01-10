from django.shortcuts import render
from django.views import View
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowProductView(View):
    template_name = 'product/show-products.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {"products": products})
    

class AddProductView(View):
    form_class = ProductForm
    initial = {"key": "value"}
    template_name = 'product/add-product.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:show-products'))
        return render(request, self.template_name, {"form": form})

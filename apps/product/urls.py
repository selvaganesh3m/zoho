from django.urls import path
from .views import AddProductView, ShowProductView


app_name = 'warehouse'

urlpatterns = [
    path('add-product/', AddProductView.as_view(), name='add-product'),
    path('show-products/', ShowProductView.as_view(), name='show-products'),
]

from django.urls import path
from .views import AddWarehouseView, ShowWarehouseView, AddWarehouseStockView, ShowWarehouseStockView


app_name = 'warehouse'

urlpatterns = [
    path('add-warehouse/', AddWarehouseView.as_view(), name='add-warehouse'),
    path('show-warehouses/', ShowWarehouseView.as_view(), name='show-warehouses'),
    path('add-stocks/', AddWarehouseStockView.as_view(), name='add-stocks'),
     path('show-stocks/', ShowWarehouseStockView.as_view(), name='show-stocks'),
]

from django.urls import path
from .views import (
    AddSalesOrderView,
    ShowSalesOrdersView,
    AddProductionOrderView,
    ShowProductionOrdersView,
    CompleteProductionOrderView,
    GenerateSalesOrderInvoiceView,
)


app_name = "order"

urlpatterns = [
    path("add-sales-order/", AddSalesOrderView.as_view(), name="add-sales-order"),
    path("show-sales-orders/", ShowSalesOrdersView.as_view(), name="show-sales-orders"),
    path(
        "add-production-order/",
        AddProductionOrderView.as_view(),
        name="add-production-order",
    ),
    path(
        "show-production-orders/",
        ShowProductionOrdersView.as_view(),
        name="show-production-orders",
    ),
    path(
        "complete-production-order/<int:order_id>/",
        CompleteProductionOrderView.as_view(),
        name="complete-production-order",
    ),
    path(
        "generate-invoice-sales-order/",
        GenerateSalesOrderInvoiceView.as_view(),
        name="generate-invoice-sales-order",
    ),
]

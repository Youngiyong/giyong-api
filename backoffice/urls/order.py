from django.urls import path
from backoffice.views.order_management import OrderListViewSet

order_urls = [
    path(r"order", OrderListViewSet.as_view({"get": "list"}), name='order-list')
]
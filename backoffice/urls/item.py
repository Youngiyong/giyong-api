from django.urls import path
from backoffice.views.item import ItemListViewSet

item_urls = [
    path(r"items/", ItemListViewSet.as_view({"get" : "list"}), name='item-list')
]
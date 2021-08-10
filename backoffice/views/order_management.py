from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from backoffice.serializers.order import OrderSerializer
from giyong.paginations import Pagination
from backoffice.models.orders import OrderShippings
from rest_framework.filters import SearchFilter

class OrderListViewSet(viewsets.GenericViewSet):
    """
    주문관리 - 마감할인
    """
    model = OrderShippings
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = []

    def get_queryset(self):
        queryset = self.model.objects.order_by("-id").all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related(
            "orderitems_set",
            )

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)


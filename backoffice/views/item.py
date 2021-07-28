from rest_framework import viewsets
from backoffice.models import SiteGoods
from backoffice.serializers.item import ItemSerializer
from giyong.responses import Response

class ItemListViewSet(viewsets.GenericViewSet):
    """
    아이템 리스트 조회
    """
    model = SiteGoods;
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, {"request": request}, many=True)

        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.data)
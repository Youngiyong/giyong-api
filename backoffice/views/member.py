from rest_framework import viewsets
from backoffice.models import Members
from backoffice.serializers.member import MemberSerializer
from giyong.responses import Response


class MemberViewSet(viewsets.GenericViewSet):
    """
    맴버 리스트 조회
    """
    model = Members;
    serializer_class = MemberSerializer
    def get_queryset(self):
        queryset = self.model.objects.get(id=389833)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, {"request": request})

        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.data)
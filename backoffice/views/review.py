from rest_framework import viewsets, generics, permissions
from backoffice.models import Members, Reviews
from backoffice.serializers import ReviewListSerializer
from giyong.responses import Response


class ReviewListViewSet(viewsets.GenericViewSet):

    """
    포스팅관리 리뷰
    """
    model = Reviews;
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None, parent=None)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related(
            "reviewimage_set"
        ).select_related(
            "item", "review_parent", "member"
        )[:100]


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        # page = self.paginate_queryset(queryset)

        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # print(page)
        # serializer = ReviewListSerializer(
        #     queryset, context={"request": request}, many=True
        # )

        return Response(data=serializer.data)
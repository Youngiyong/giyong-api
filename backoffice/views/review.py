from rest_framework import viewsets, generics, permissions
from backoffice.models import Members, Reviews
from backoffice.serializers import ReviewListSerializer
from giyong.paginations import BackOfficePaginator
from giyong.responses import Response


class ReviewListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 리뷰
    """
    model = Reviews;
    serializer_class = ReviewListSerializer
    permission_classes = [TokenHasScope]
    pagination_class = BackOfficePagination
    required_scopes = ["BACKOFFICE"]

    filter_backends = [DjangoFilterBackend, SearchFilter]

    data = requests
    search_fields = []
    # filterset_class = ReviewListFilter

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None, parent=None)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related(
            "reviewimage_set"
        ).select_related(
            "item", "review_parent", "member"
        )

        search_filter = self.request.GET.get("search_filter")
        date_filter = self.request.GET.get("date_filter")

        fields = {
            "members.name": "member__name",
            "members.cp": "member__mobile",
            "reviews.member_id": "member__id",
            "reviews.content": "contents",
            "items.name": "item__name",
            "reviews.item_id": "item__id",
            "shops.name": "item__shop__name",
            "shops.id": "item__shop__id",
            # "reviews.created_at": "item__shop__name"
        }

        if search_filter is not None:
            self.search_fields.append(fields[search_filter])

        if date_filter is not None:
            # self.search_fields.append(fields[date_filter])
            start = self.request.GET.get("start_at")
            end = self.request.GET.get("end_at")

            if start and not end:
                queryset = queryset.filter(
                    created__at__date__gte=start
                ).values("created_at")

            if not start and end:
                queryset = queryset.filter(
                    created__at__date__lte=end
                )

            if start and end:
                queryset = queryset.filter(
                    created_at__date__gte=start,
                    created_at__date__lte=end
                ).values("created_at")

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(page, many=True)

        return Response(data=serializer.data)

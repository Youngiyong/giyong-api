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

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None, parent=None)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related(
            "reviewimage_set"
        ).select_related(
            "item", "review_parent", "member"
        )[:100]

        pageNumber = int(request.GET.get("page", 1) or 1)

        paginator = BackOfficePaginator(queryset, 25)
        page = paginator.page(pageNumber)


        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data, page=page.paginator)
        # if page is not None:
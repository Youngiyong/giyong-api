from rest_framework import viewsets, generics, permissions
from backoffice.models import Members
from backoffice.serializers.member import MemberSerializer
from giyong.responses import Response


class ReviewListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 리뷰
    """
    # model = Reviews;
    model = Members;
    # permission_classes = (TokenHasScope,)
    serializer_class = MemberSerializer
    def get_queryset(self):
        queryset = self.model.objects.get(id=389833)
        #     self.model.objects.prefetch_related(
        #         "reviewimage_set", "item__itemimages_set"
        #     )용
        #         .select_related(
        #         "item", "item__shop", "item__item_number", "member", "review_parent"
        #     )[:10]
        # )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, {"request": request})

        serializer.is_valid(raise_exception=True)
        # page = self.paginate_queryset(queryset)
        # serializer = BackOfiiceReviewSerializer(
        #     queryset, context={"request": request}, many=True
        # )
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # print(page)
        # serializer = ReviewListSerializer(
        #     queryset, context={"request": request}, many=True
        # )

        return Response(data=serializer.data)
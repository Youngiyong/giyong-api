from django_filters import rest_framework as filters

from backoffice.models import Reviews


class ReviewFilter(filters.FilterSet):
    """
        리뷰 필터링
    """

    image = filters.BooleanFilter(method="get_image", help_text="사진리뷰 필터")
    reply = filters.BooleanFilter(method="get_reply", help_text="사장님 댓글필터")
    date = filters.DateFromToRangeFilter(field_name="created_at", help_text="날짜필터")

    class Meta:
        model = Reviews
        fields = "__all__"

    def get_image(self, queryset, name, value):
        if value is True:
            queryset = queryset.filter(reviewimage__isnull=False)
        return queryset

    def get_reply(self, queryset, name, value):
        if value is True:
            queryset = queryset.filter(review_parent__isnull=True)
        return queryset

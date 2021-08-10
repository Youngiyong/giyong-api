from django_filters import rest_framework as filters




class OrderListFilter(filters.FilterSet):
    """
        주문 날짜 필터
    """
    pass

class ReviewListFilter(filters.FilterSet):
    """
        백오피스 리뷰 관리 필터링
    """
    created_at = filters.DateFromToRangeFilter(method="get_date", help_text="날짜필터")

    def get_date(self, queryset, name, value):
        if value:
            date = value
            start = date.start_at
            end = date.end_at
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

            return queryset

from rest_framework import pagination
from responses import Response

class Pagination(pagination.PageNumberPagination):
    """

    """
    page_size_query_param = 'limit'

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                return _positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size

    def paginate_queryset(self, queryset, request, view=None):
        # page_size를 가져옵니다.
        page_size = self.get_page_size(request)
        if not page_size:
            return None
        """ django_paginator_class는 django의 Paginator (django/core/paginator.py) 클래스로 pagination의 전체 동작을 담당합니다.
        page_size와 queryset을 pagniator 객체를 선언합니다. """
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)

        # 가져온 paginator중에서 사용자가 지정한 페이지를 가져 옵니다.
        self.page = paginator.page(page_number)

        return list(self.page)

    def get_paginated_response(self, data):

        return Response({
            'items': data,
            'pagination': {
                "path": "{}{}".format(settings.BASE_URL, self.request.path),
                "perPage": len(data),
                "count": self.page.paginator.per_page,
                "total": self.page.paginator.count,
                "currentPage": self.page.number,
                "lastPage": self.page.paginator.num_pages,
                "previousPageUrl": self.get_previous_link(),
                'nextPageUrl': self.get_next_link()
            }
        })



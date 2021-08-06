from rest_framework import pagination
from responses import Response

class Pagination(pagination.PageNumberPagination):
    """

    """

    page_size_query_param = 'limit'

    def get_paginated_response(self, data):

        return Response(items=data, pagination=
            {
                "path": "{}{}".format(settings.BASE_URL, self.request.path),
                "perPage": len(data),
                "count": self.page.paginator.per_page,
                "total": self.page.paginator.count,
                "currentPage": self.page.number,
                "lastPage": self.page.paginator.num_pages,
                "previousPageUrl": self.get_previous_link(),
                'nextPageUrl': self.get_next_link()
            }
        )
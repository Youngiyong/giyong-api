from rest_framework import pagination
from responses import Response

class Pagination(pagination.PageNumberPagination):
    """

    """

    page_size_query_param = 'limit'
    page_size = 25
    def get_paginated_response(self, data):

        return Response(data=data, pagination=
            {
                "path": "{}{}".format(settings.BASE_URL, self.request.path),
                "perPage": self.page.paginator.per_page,
                "count": self.page.paginator.count,
                "total": len(data),
                "currentPage": self.page.number,
                "lastPage": self.page.paginator.num_pages,
                "previousPageUrl": self.get_previous_link(),
                'nextPageUrl': self.get_next_link()
            }
        )
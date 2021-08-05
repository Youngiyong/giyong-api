from rest_framework import pagination
from responses import Response

class Pagination(pagination.PageNumberPagination):
    """

    """
    page_size = 25
    page_size_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):

        page = {
            "path": self.page_size_query_param,
            "perPage": self.page.paginator.per_page,
            "count": self.page.paginator.per_page,
            "total": self.page.paginator.count,
            "currentPage": int(self.request.GET.get("page", 1) or 1),
            "lastPage": self.max_page_size,
            "previousPageUrl": self.get_previous_link(),
            'nextPageUrl': self.get_next_link()
        }
        # test = {
        #     'path': self.get_previous_link(),
        #     'perPage': self.page.number,
        #     'count': self.page.count,
        #     'total': self.page.count,
        #     'currentPage': self.page_size,
        #     'lastPage': "",
        #     'previousPageUrl': "",
        #     'nextPageUrl': self.get_next_link()
        # }
        # page = json.dumps(test)

        return Response(
            data=data,
            page=page
        )


from django.core.paginator import Paginator
from rest_framework import pagination
from giyong.responses import Response


class RawPageNumberPagination(Paginator):
    def __init__(self, object_list, per_page, count, **kwargs):
        super().__init__(object_list, per_page, **kwargs)
        self.raw_count = count

    def _get_count(self):
        return self.raw_count
        count = property(_get_count)

    def page(self, number):
        number = self.validate_number(number)
        return self._get_page(self.object_list, number, self)

class BackOfficePaginator(Paginator):
    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        self.object_list = object_list
        self._check_object_list_is_ordered()
        self.per_page = int(per_page)
        self.orphans = int(orphans)
        self.allow_empty_first_page = allow_empty_first_page

class PageNumberPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data, page=None, has_next=None, count=None):
        return Response(
            data=data,
            count=count if count else self.page.paginator.count,
            has_next=has_next if has_next else self.page.has_next(),
            page=page if page else self.page.number
        )
        # return LastorderResponse(data={
        #         'links': {
        #             'next': self.get_next_link(),
        #             'previous': self.get_previous_link()
        #         },
        #         'count': self.page.paginator.count,
        #         'results': data
        # })

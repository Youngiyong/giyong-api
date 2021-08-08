
from rest_framework import viewsets, permissions

from giyong.responses import Response

from backoffice.models import Post
from giyong.paginations import Pagination

from backoffice.serializers.post import PostListSerializer
from rest_framework.filters import SearchFilter

class PostListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 리스트
    """
    model = Post
    serializer_class = PostListSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination

    filter_backends = [SearchFilter]
    search_fields = []

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None)
        return queryset

    def list(self, request, *args, **kwargs):
        board_id = self.request.GET.get("board_id", 1)

        queryset = self.get_queryset().select_related(
            "board", "shop", "category"
        ).filter(board_id=board_id)

        search_filter = self.request.GET.get("search_filter")
        date_filter = self.request.GET.get("date_filter")

        fields = {
            "posts.content": "content",
            "posts.title": "title",
        }

        if search_filter is not None:
            self.search_fields.append(fields[search_filter])

        if date_filter == "posts.created_at":
            start = self.request.GET.get("start_at")
            end = self.request.GET.get("end_at")

            if start and not end:
                start = start.replace("+", " ")
                queryset = queryset.filter(
                    created_at__gte=start
                )

            if not start and end:
                end = end.replace("+", " ")
                queryset = queryset.filter(
                    created_at__lte=end
                )

            if start and end:
                start = start.replace("+", " ")
                end = end.replace("+", " ")
                queryset = queryset.filter(
                    created_at__gte=start,
                    created_at__lte=end
                )

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(page, many=True)

        return Response(data=serializer.data)

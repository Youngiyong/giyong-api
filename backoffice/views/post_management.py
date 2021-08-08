
from rest_framework import viewsets, generics, permissions

from giyong.responses import BackOfficeResponse, BackOfficeException
from backoffice.serializers.post import PostListSerializer
from backoffice.serializers.board import BoardListSerializer, BoardSerializer
from backoffice.models import Reviews, Post, Board
from giyong.paginations import Pagination

from backoffice.serializers.review import ReviewListSerializer
from rest_framework.filters import SearchFilter

class BoardListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 보드(설정)
    """
    model = Board;
    serializer_class = BoardListSerializer
    # permission_classes = [TokenHasScope]
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination
    # required_scopes = ["BACKOFFICE"]

    filter_backends = [SearchFilter]
    search_fields = []

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None).all().order_by("-id")
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related("boardcategory_set").select_related("section_code")

        search_filter = self.request.GET.get("search_filter")
        date_filter = self.request.GET.get("date_filter")

        fields = {
            "boards.name": "name",
        }

        if search_filter is not None:
            self.search_fields.append(fields[search_filter])

        if date_filter == "boards.created_at":
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

        return BackOfficeResponse(data=serializer.data)
    pass

class ReviewListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 리뷰 리스트(리뷰)
    """
    model = Reviews;
    serializer_class = ReviewListSerializer
    # permission_classes = [TokenHasScope]
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination
    # required_scopes = ["BACKOFFICE"]

    filter_backends = [SearchFilter]
    search_fields = []

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None, parent=None)
        return queryset

    """
    리뷰 보여짐 여부 업데이트
    """

    def updateVisible(self, request, *args, **kwargs):
        data = request.data
        try:
            instance = self.model.objects.get(id=data.get('id'))
            instance.is_visible = data.get('is_visible')
            instance.save()

        except Reviews.DoesNotExist:
            raise BackOfficeException(code="S0010", detail="등록되지 않은 리뷰 번호입니다.")

        return BackOfficeResponse()

    def destroy(self, request, *args, **kwargs):
        data = request.data

        try:
            instance = self.model.objects.get(id=data.get('id'))
            instance.delete()

        except Reviews.DoesNotExist:
            raise BackOfficeException(code="S0010", detail="등록되지 않은 리뷰 번호입니다")

        return BackOfficeResponse()
    """
    리뷰 리스트
    """
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related(
            "reviewimage_set"
        ).select_related(
            "item", "review_parent", "member"
        )

        search_filter = self.request.GET.get("search_filter")
        date_filter = self.request.GET.get("date_filter")

        fields = {
            "members.name": "member__name",
            "members.cp": "member__mobile",
            "reviews.member_id": "member__id",
            "reviews.content": "contents",
            "items.name": "item__name",
            "reviews.item_id": "item__id",
            "shops.name": "item__shop__name",
            "shops.id": "item__shop__id",
        }

        if search_filter is not None:
            self.search_fields.append(fields[search_filter])

        if date_filter == "reviews.created_at":
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

        return BackOfficeResponse(data=serializer.data)

class PostListViewSet(viewsets.GenericViewSet):
    """
    포스팅관리 포스트 리스트(스토어)
    """
    model = Post
    serializer_class = PostListSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination

    filter_backends = [SearchFilter]
    search_fields = []

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at=None).order_by("-id")
        return queryset

    """
    단일 조회
    """

    def retrieve(self, request, *args, **kwargs):
        board_id = self.request.GET.get("board_id")

        instance = Board.objects.select_related("section_code").filter(id=board_id).first()

        if instance is None:
            raise BackOfficeException(code="S0010", detail="등록되지 않은 보드 번호입니다")

        serializer = BoardSerializer(instance)
        return BackOfficeResponse(data=serializer.data)

    """
    리스트 조회
    """
    def list(self, request, *args, **kwargs):
        board_id = self.request.GET.get("board_id", 1)

        queryset = self.get_queryset().select_related(
            "board", "shop", "category"
        ).filter(board_id=board_id)

        search_filter = self.request.GET.get("search_filter")
        date_filter = self.request.GET.get("date_filter")

        fields = {
            "posts.contents": "contents",
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

        return BackOfficeResponse(data=serializer.data)
from django.urls import path
from backoffice.views.post_management import BoardListViewSet

board_urls = [
    path(r"board", BoardListViewSet.as_view({'get':'list'}), name='post-list'),
]
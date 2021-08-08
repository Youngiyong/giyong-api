from django.urls import path
from backoffice.views.post import PostListViewSet

post_urls = [
    path(r"post", PostListViewSet.as_view({'get':'list'}), name='post-list'),
]
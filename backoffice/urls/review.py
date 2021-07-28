from django.urls import path
from backoffice.views.review import ReviewListViewSet

review_urls = [
    path(r"review/", ReviewListViewSet.as_view({'get':'list'}), name='review-list')
]
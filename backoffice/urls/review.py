from django.urls import path
from backoffice.views.review import ReviewListViewSet

review_urls = [
    path(r"review/", ReviewListViewSet.as_view({'get':'list'}), name='review-list'),
    path(r"review/update/visible", ReviewListViewSet.as_view({'put': 'updateVisible'}, name='update-visible')),
    path(r"review/delete", ReviewListViewSet.as_view({'delete': 'destroy'}, name='destroy'))
]
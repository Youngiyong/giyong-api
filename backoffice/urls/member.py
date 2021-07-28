from django.urls import path
from backoffice.views.member import MemberViewSet

member_urls = [
    path(r"users/", MemberViewSet.as_view({"get" : "list"}), name='member-list')
]
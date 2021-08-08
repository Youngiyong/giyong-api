from backoffice.urls.review import review_urls
from backoffice.urls.member import member_urls
from backoffice.urls.item import item_urls
from backoffice.urls.board import board_urls
from backoffice.urls.post import post_urls
app_name = "bo"

urlpatterns = []

urlpatterns += review_urls
urlpatterns += member_urls
urlpatterns += item_urls
urlpatterns += post_urls
urlpatterns += board_urls
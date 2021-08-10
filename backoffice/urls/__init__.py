from backoffice.urls.post import post_urls
from backoffice.urls.review import review_urls
from backoffice.urls.board import board_urls
from backoffice.urls.order import order_urls

app_name = "bo"

urlpatterns = []
urlpatterns += review_urls
urlpatterns += post_urls
urlpatterns += order_urls
urlpatterns += board_urls

from backoffice.urls.review import review_urls
from backoffice.urls.member import member_urls
from backoffice.urls.item import item_urls
app_name = "bo"

urlpatterns = []

urlpatterns += review_urls
urlpatterns += member_urls
urlpatterns += item_urls

from django.urls import path
from .views import ShortenUrlView, RedirectView, URLListView

app_name = 'url'

urlpatterns = [
    path('', ShortenUrlView.as_view(), name='shorten'),
    path('url_list/', URLListView.as_view(), name="url_list"),
    path('<str:short_code>/', RedirectView.as_view(), name="url_redirect"),
]


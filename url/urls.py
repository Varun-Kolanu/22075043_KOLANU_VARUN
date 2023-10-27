from django.urls import path
from .views import ShortenUrlView, RedirectView, URLListView

app_name = 'url'

urlpatterns = [
    path('', ShortenUrlView, name='shorten'),
    path('url_list/', URLListView, name="url_list"),
    path('<str:short_code>/', RedirectView, name="url_redirect"),
]


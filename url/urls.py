from django.urls import path
from .views import ShortenUrlView, RedirectView

app_name = 'url'

urlpatterns = [
    path('', ShortenUrlView, name='shorten'),
    path('<str:short_code>/', RedirectView)
]


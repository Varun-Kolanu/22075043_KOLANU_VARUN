from django.urls import path
from .views import ShortenUrl

app_name = 'url'

urlpatterns = [
    path('', ShortenUrl, name='shorten')
]


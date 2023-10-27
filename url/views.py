import random, string
from django.shortcuts import render
from .models import URL
from django.http import HttpResponse

# Create your views here.

def unique_short_code(length=6):
    """
    Returns a unique short code for a given length
    """
    while True:
        short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        if not URL.objects.filter(short_code=short_code).exists():
            return short_code

def sample(request):
    return HttpResponse(unique_short_code(6))

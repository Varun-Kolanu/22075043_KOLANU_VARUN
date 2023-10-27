import random, string
from django.shortcuts import render, get_object_or_404, redirect
from .models import URL
from django.http import HttpResponse
from .forms import URLForm
from url_shortener.settings import SITE_URL
from django.views import generic

# Create your views here.

def unique_short_code(length=6):
    """
    Returns a unique short code for a given length
    """
    while True:
        short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        if not URL.objects.filter(short_code=short_code).exists():
            return short_code

def ShortenUrlView(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')
            url_in_db = URL.objects.filter(long_url=long_url).first()
            if url_in_db:
                data = {
                    'form': form,
                    'shortened_url': SITE_URL + "/" + url_in_db.short_code,
                }
                return render(request, 'url/home.html', data)
            short_code = unique_short_code(6)
            URL.objects.create(long_url=long_url, short_code=short_code)
            data = {
                'form': form,
                'shortened_url': SITE_URL + "/" + short_code,
            }
            return render(request, 'url/home.html', data)
        else:
            data = {
                'form': form
            }
            return render(request, 'url/home.html', data)

    if request.method == 'GET':
        form = URLForm()
        return render(request, 'url/home.html', {'form': form})


def RedirectView(request, short_code):
    url_obj = get_object_or_404(URL,short_code=short_code)
    print(url_obj)
    return redirect(url_obj.long_url)

def URLListView(request):
    url_objs = URL.objects.all()
    data = {
        'url_objs': url_objs,
        'site_url': SITE_URL
    }
    return render(request, 'url/list.html', data)

from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm


def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:login'))  # НЕПРАВИЛЬНЫЙ АДРЕС

    template = 'shortener/index.html'

    context = {}

    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save(commit=False)
            shortened_object.user = request.user
            shortened_object.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            # new_url = request.get('/') + shortened_object.short_url

            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url


            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken :(')


def urls_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:login'))  # НЕПРАВИЛЬНЫЙ АДРЕС

    template = 'shortener/urls_list.html'

    urls = Shortener.objects.filter(user=request.user).order_by('id')
    my_site_url = request.build_absolute_uri('/')

    context = {
        'urls': urls,
        'my_site_url':my_site_url
    }

    return render(request, template, context)

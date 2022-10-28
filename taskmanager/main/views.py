from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Photos


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def photography(request, photo_id):
    photo = Photos.objects.get(pk=photo_id)
    if photo is not None:
        return render(request, 'main/photography.html', {'photo': photo})
    else:
        raise Http404('Photo does not exist')

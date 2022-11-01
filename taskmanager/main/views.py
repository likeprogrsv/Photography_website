import imp
from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Photos
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm

num_rand_photos = 6


def loginUser(request):
    page ='login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request): 
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('home')
        
    context = {'form': form, 'page': page}
    return render(request, 'main/login_register.html', context)


def index(request):
    all_photos = Photos.objects.all()
    random_photos = random.sample(list(all_photos), num_rand_photos)
    context = {'all_photos': all_photos, 'random_photos': random_photos}
    return render(request, 'main/index.html', context)

@login_required(login_url='login')
def about(request):
    return render(request, 'main/about.html')


def photography(request, photo_id):
    photo = Photos.objects.get(pk=photo_id)
    if photo is not None:
        return render(request, 'main/photography.html', {'photo': photo})
    else:
        raise Http404('Photo does not exist')

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Photos, Comment
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CommentForm
from django.db.models import Func, F, Count
# from django.contrib.auth.forms import UserCreationForm

# num_rand_photos = 1


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


def index(request, num_rand_photos=6):
    all_photos = Photos.objects.all()
    if all_photos.count() >= num_rand_photos:
        random_photos = random.sample(list(all_photos), num_rand_photos)        
    else: 
        random_photos = random.sample(list(all_photos), all_photos.count())
    context = {'all_photos': all_photos, 'random_photos': random_photos}
    return render(request, 'main/index.html', context)

# @login_required(login_url='login')
def about(request):
    return render(request, 'main/about.html')


def photos(request):    
    query_tags = Photos.objects.annotate(tag=Func(F('category'), function='unnest'))\
        .values('tag', 'id').order_by('tag').annotate(count=Count('id')).values('id', 'tag', 'count')   
    tags={}    
    for tag in query_tags:
        if tag['tag'] in tags:
            tags[tag['tag']]['ids'].append(tag['id'])
            tags[tag['tag']]['count'] += 1 
        else:
            tags[tag['tag']] = {'ids': [tag['id']], 'count': tag['count']}        
    tag_counts = {t: tags[t]['count'] for t in tags}
    
    """ Make sections for 3 types of tags """
    bottom_layer, top_layer = 0, 0    
    if len(tag_counts) > 0:       
        tag_count_max = tag_counts[max(tag_counts, key=tag_counts.get)]
        tag_count_min = tag_counts[min(tag_counts, key=tag_counts.get)]
        bottom_layer = tag_count_min + (( tag_count_max - tag_count_min) * 0.33)
        top_layer = tag_count_min + (( tag_count_max - tag_count_min) * 0.66)

    curr_tag = request.GET.get('curr_tag')
    if curr_tag is None:
        photos = Photos.objects.all()
    else:
        photos = Photos.objects.filter(pk__in=tags[curr_tag]['ids'])    

    context = {'photos': photos, 'tags': tag_counts, 'bottom_layer': bottom_layer, 'top_layer': top_layer}
    return render(request, 'main/photos.html', context)


def photography(request, photo_id):
    photo = Photos.objects.get(pk=photo_id)
    photo_comments = Comment.objects.all().filter(photo=photo.id)

    form = CommentForm
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.photo = photo
                form.save()
                return redirect('photos')
            else: print('comment is invalid')
        else: return redirect('login')
    if photo is not None:
        return render(request, 'main/photography.html', {'photo': photo, 'photo_comments': photo_comments, 'form': form})
    else:
        raise Http404('Photo does not exist')

    
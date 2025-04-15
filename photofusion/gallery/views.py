from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PhotoForm, ProfileForm
from .models import Photo, Album, Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q


@login_required
def home(request):
    album_id = request.GET.get('album')
    query = request.GET.get('q')

    photos = Photo.objects.filter(album__user=request.user)

    if album_id:
        photos = photos.filter(album__id=album_id)

    if query:
        photos = photos.filter(
            Q(caption__icontains=query) |
            Q(album__name__icontains=query)
        )

    paginator = Paginator(photos.order_by('-uploaded_at'), 8)
    page_number = request.GET.get('page')
    photos_page = paginator.get_page(page_number)

    albums = Album.objects.filter(user=request.user)
    return render(request, 'gallery/home.html', {
        'photos': photos_page,
        'albums': albums,
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'gallery/register.html', {'form': form})

def login_view(request):
    error = False
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            Profile.objects.get_or_create(user=user)
            return redirect('home')
        else:
            error = True
    return render(request, 'gallery/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            album = form.cleaned_data.get('album')
            new_album_name = form.cleaned_data.get('new_album')

            if not album and not new_album_name:
                form.add_error('album', "Please select an existing album or enter a new one.")
            else:
                if new_album_name:
                    album, _ = Album.objects.get_or_create(name=new_album_name, user=request.user)

                photo = form.save(commit=False)
                photo.album = album
                photo.save()
                return redirect('home')
    else:
        form = PhotoForm(user=request.user)
    return render(request, 'gallery/upload.html', {'form': form})

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if photo.album.user != request.user:
        return HttpResponseForbidden()
    photo.delete()
    return redirect('home')

@login_required
def edit_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if photo.album.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm(instance=photo, user=request.user)
    return render(request, 'gallery/upload.html', {'form': form})

@login_required
def edit_profile(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'gallery/edit_profile.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('login')
    return render(request, 'gallery/delete_account.html')

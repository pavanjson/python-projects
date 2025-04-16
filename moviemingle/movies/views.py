from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'movies/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'movies/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




def index(request):
    query = request.GET.get('q')
    if query:
        movies_list = Movie.objects.filter(title__icontains=query)
    else:
        movies_list = Movie.objects.all()

    paginator = Paginator(movies_list, 6)  # 6 movies per page
    page_number = request.GET.get("page")
    movies = paginator.get_page(page_number)

    return render(request, 'movies/index.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    existing_review = Review.objects.filter(movie=movie, reviewer=request.user.username).first()

    if request.method == 'POST' and not existing_review:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.reviewer = request.user.username
            review.rating = request.POST.get("rating")
            review.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'form': form,
        'existing_review': existing_review,
    })

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

@user_passes_test(is_admin)
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_detail', pk=pk)
    return render(request, 'movies/movie_form.html', {'form': form})

@user_passes_test(is_admin)
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})



@login_required
def toggle_favorite(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.favorites.filter(id=request.user.id).exists():
        movie.favorites.remove(request.user)
    else:
        movie.favorites.add(request.user)
    return HttpResponseRedirect(reverse('movie_detail', args=[pk]))

@login_required
def edit_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, movie=movie, reviewer=request.user.username)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.rating = request.POST.get("rating")
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'movies/edit_review.html', {'form': form, 'movie': movie, 'review': review,})


@login_required
def delete_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, movie=movie, reviewer=request.user.username)

    if request.method == 'POST':
        review.delete()
        return redirect('movie_detail', pk=movie.pk)

    return render(request, 'movies/delete_review.html', {'review': review, 'movie': movie})

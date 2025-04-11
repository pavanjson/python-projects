# core/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, PostForm, CommentForm
from .models import Profile, Post, Follow, Like, Comment


from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        following_ids = Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
        posts = Post.objects.filter(user_id__in=following_ids).order_by('-timestamp')
        following_users = User.objects.filter(id__in=following_ids)
        return render(request, 'home.html', {
            'posts': posts,
            'following_users': following_users,
        })
    else:
        context = {
            'images': ['images/image1.jpeg', 'images/image2.jpeg', 'images/image3.jpeg'],
            'videos': ['videos/video1.mp4', 'videos/video2.mp4'],
        }
        return render(request, 'home.html', context)

# Register

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now login.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

    # Login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')


# Logout

def user_logout(request):
    logout(request)
    return redirect('login')


# Profile

@login_required
def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user_obj).order_by('-timestamp')
    is_following = Follow.objects.filter(follower=request.user, following=user_obj).exists()
    return render(request, 'profile.html', {'user_obj': user_obj, 'posts': posts, 'is_following': is_following})


# Follow

@login_required
def follow_user(request, username):
    to_follow = get_object_or_404(User, username=username)
    Follow.objects.get_or_create(follower=request.user, following=to_follow)
    return redirect('profile', username=username)


# Unfollow

@login_required
def unfollow_user(request, username):
    to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=to_unfollow).delete()
    return redirect('home')  # 👈 Redirect to home instead of profile

# Create Post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile', username=request.user.username)
    else:
        form = PostForm()
    return render(request, 'registration/create_post.html', {'form': form})

# Like Post

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('home')


# Comment on Post

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'registration/comment_post.html', {'form': form, 'post': post})

@login_required
def search_users(request):
    query = request.GET.get('q')
    users = User.objects.filter(username__icontains=query).exclude(username=request.user.username)
    return render(request, 'registration/search_results.html', {'users': users, 'query': query})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        post.delete()
    return redirect('profile', username=request.user.username)
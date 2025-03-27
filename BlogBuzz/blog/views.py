from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Comment, Tag
from .forms import CommentForm, PostForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    # Paginate posts (e.g., 5 posts per page)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'query': query})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(is_spam=False).order_by('-created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save post
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Process tags input
            tags_str = form.cleaned_data.get('tags')
            if tags_str:
                tag_names = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)
            messages.success(request, "Post created successfully.")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            # Update tags: clear and then add new ones
            post.tags.clear()
            tags_str = form.cleaned_data.get('tags')
            if tags_str:
                tag_names = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)
            messages.success(request, "Post updated successfully.")
            return redirect('post_detail', pk=post.pk)
    else:
        # Prepopulate the tags field as a comma-separated string
        initial_tags = ", ".join([tag.name for tag in post.tags.all()])
        form = PostForm(instance=post, initial={'tags': initial_tags})
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('post_list')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('post_list')

# --- New Views for Enhanced Features ---

@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.info(request, "You unliked the post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "You liked the post.")
    return redirect('post_detail', pk=pk)

@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('post_detail', pk=comment.post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('post_detail', pk=comment.post.pk)
    if request.method == 'POST':
        post_id = comment.post.pk
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('post_detail', pk=post_id)
    return render(request, 'blog/delete_comment.html', {'comment': comment})

# PortfolioPro/apps/blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


def blog_list(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-published_date')

    context = {'posts': posts, 'user': user}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, username, pk):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=pk, author=user)

    context = {'post': post, 'user': user}
    return render(request, 'blog/blog_detail.html', context)


@login_required
def create_post(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "You are not authorized to create a post for this user.")
        return redirect('blog:blog_list', username=request.user.username)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('blog:blog_list', username=user.username)
    else:
        form = PostForm()

    context = {'form': form, 'user': user}
    return render(request, 'blog/create_post.html', context)


@login_required
def edit_post(request, username, pk):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=pk, author=user)

    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('blog:blog_detail', username=username, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('blog:blog_detail', username=username, pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {'form': form, 'post': post, 'user': user}
    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, username, pk):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=pk, author=user)

    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog:blog_detail', username=username, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('blog:blog_list', username=username)

    context = {'post': post, 'user': user}
    return render(request, 'blog/confirm_delete.html', context)

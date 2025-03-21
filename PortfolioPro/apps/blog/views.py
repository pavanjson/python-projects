from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


def blog_list(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the logged-in user as the author
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('blog:blog_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Check that the logged-in user is the author
    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('blog:blog_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('blog:blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Check that the logged-in user is the author
    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog:blog_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('blog:blog_list')

    # Render a confirmation page on GET
    return render(request, 'blog/confirm_delete.html', {'post': post})

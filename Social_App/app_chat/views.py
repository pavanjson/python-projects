from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from .models import ChatGroup, GroupMessage
from .forms import GroupMessageForm

def inbox(request):
    # This slug is manual right now.
    manual_slug = "mirpur-protesters-1"

    the_group = get_object_or_404(ChatGroup, slug=manual_slug)
    grp_messages = GroupMessage.objects.filter(group=the_group)

    if request.method =="POST":
        form = GroupMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = the_group
            message.save()
            return redirect(request.path)
    else:
        form = GroupMessageForm()

    context={
        "form":form,
        "grp_messages":grp_messages
    }
    return render(request, "chat/main/messenger.html", context)

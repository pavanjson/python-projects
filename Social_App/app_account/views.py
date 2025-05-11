from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from app_users.models import Profile, User
from app_home.models import Friends, PostImage
from app_users.forms import ProfileForm
from django.contrib import messages
from app_home.utilities import login_requirements
import time

from .forms import FriendPrivacy


# 21/08/2024
@login_requirements()
def delete_account(request):
    confirm = request.GET.get("confirmation")

    if confirm=='on':
        user = request.user
        messages.warning(request,"Your Account is being deleted!")
        time.sleep(5)
        user.delete()
        messages.error(request,"Your Account is deleted permanently!")
        return redirect("homepage")
    else:
        return render(request, "settings/main/delete_account.html")

# 20-07-2024 ----- (DONE)
@login_requirements()
def settings(request):
    return render(request, "settings/main/settings.html")


# 20-07-2024 ----- (DONE)
# IMPROVE: 3
# ERROR: Here as i used HTMX so form saves good but image don't -- Need Fix
@login_requirements()
def setting_tabs(request, option):
    if request.htmx:
        profile=request.user.profile
        if option=="profile":
            if request.method == "POST":
                form = ProfileForm(request.POST, request.FILES, instance=profile)                
                if form.is_valid():
                    form.save()
                    messages.success(request,"Profile was updated successfully!")
                    return redirect("setting_tabs", option="profile")
                else:
                    print(form.errors)
            else:
                form = ProfileForm(instance=profile)
            context = {"form":form}

            return render(request,"settings/partials/profile.html", context)
        
        elif option=="notify":
            
            return render(request,"settings/partials/notify.html")
        
        elif option=="suspend":
            
            return render(request,"settings/partials/delete.html")
        
        elif option=="privacy":
            try:
                friend_setting = Friends.objects.get(author__user=request.user)
            except:
                friend_setting = None
            if friend_setting is not None:
                if request.method=="POST":
                    form = FriendPrivacy(request.POST, instance=friend_setting)
                    if form.is_valid():
                        form.save()

                        return redirect(request.path)
                else:
                    form = FriendPrivacy(instance=friend_setting)
            else:
                form= None
            context={"form":form}
            return render(request,"settings/partials/privacy.html", context)
        
    return HttpResponse("Are you losted? Go back where you came from!")


# 23/07/2024 --- (DONE)
@login_requirements()
def friends(req, cx_user):
    '''
    This function first filter out the friend list of the requested user,
    then if the current logged in user is in the friend list then 
    based on the privacy demanded response will be shown.

    '''
    user = get_object_or_404(User, username=cx_user )
    profile=user.profile
    all_friends = get_object_or_404(Friends, author=profile)
    if all_friends.privacy=='friends':
        if req.user.profile not in all_friends.friend.all():
            public_friends = None
    else:
        public_friends = None if all_friends.privacy=="only_me" else all_friends.friend.all()
    context={
        "friends":public_friends,
    }
    return render(req, "settings/main/friends.html", context)

# 23/07/2024 --- (DONE)
@login_requirements()
def photos(req, cx_user):
    '''
    This function first filter out the friend list of the requested user,
    then if the current logged in user is in the friend list then 
    based on the privacy demanded response will be shown.

    '''
    user = get_object_or_404(User, username=cx_user ) #requested user
    profile=user.profile #requested user profile
    all_friends = get_object_or_404(Friends, author=profile)

    if req.user.profile == profile:
        public_photo=PostImage.objects.filter(post__author = profile )
    else:
        if req.user.profile in all_friends.friend.all():
            public_photo = PostImage.objects.filter(post__author = profile ,post__privacy='friends')
        else:
            public_photo = PostImage.objects.filter(post__author = profile ,post__privacy='public')
    
    context={
        "photos":public_photo,
    }
    return render(req, "settings/main/photos.html", context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, HttpResponse
from app_users.models import Profile

def login_requirements():
    def outer(function_in_view):
        @login_required()
        def wrapper_func(request, *args, **kwargs):
            try:
                profile = request.user.profile
            except:
                profile = Profile.objects.create(user=request.user)
                profile.save()
                return redirect("signup_details")
            
            if profile.registered:
                return function_in_view(request, *args, **kwargs)
            else:
                return redirect("signup_details")

        return wrapper_func
    return outer


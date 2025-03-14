from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Company, Application, UserProfile
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserProfileForm

def job_list(request):
    jobs = Job.objects.all().order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    # Check if the authenticated user has already applied
    has_applied = False
    if request.user.is_authenticated:
        has_applied = job.applications.filter(user=request.user).exists()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()

    context = {
        'job': job,
        'form': form,
        'has_applied': has_applied,  # pass the variable to the template
    }
    return render(request, 'jobs/job_detail.html', context)

def company_profile(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    jobs = company.jobs.all()
    return render(request, 'jobs/company_profile.html', {'company': company, 'jobs': jobs})

@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'jobs/user_profile.html', {'profile': profile})

def signup(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
              user = form.save()
              login(request, user)
              return redirect('job_list')
    else:
         form = UserCreationForm()
    return render(request, 'jobs/signup.html', {'form': form})

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'jobs/edit_profile.html', {'form': form})

@login_required
def my_applications(request):
    # Retrieve all applications submitted by the current user
    applications = Application.objects.filter(user=request.user).select_related('job', 'job__company')
    context = {
        'applications': applications,
    }
    return render(request, 'jobs/my_applications.html', context)
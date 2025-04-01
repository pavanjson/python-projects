from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Poll, PollOption, Vote
from .forms import RegistrationForm, PollCreationForm, PollOptionForm
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'polls/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect based on role
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return render(request, 'polls/login.html', {'error': 'Invalid credentials.'})
    return render(request, 'polls/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    polls = Poll.objects.all()
    return render(request, 'polls/admin_dashboard.html', {'polls': polls})


@login_required
def user_dashboard(request):
    polls = Poll.objects.all()  # Optionally filter active polls
    return render(request, 'polls/user_dashboard.html', {'polls': polls})


@login_required
def poll_create(request):
    # Only allow superusers to create polls
    if not request.user.is_superuser:
        return redirect('poll_list')

    OptionFormSet = modelformset_factory(PollOption, form=PollOptionForm, extra=2)
    if request.method == 'POST':
        form = PollCreationForm(request.POST, request.FILES)
        formset = OptionFormSet(request.POST, queryset=PollOption.objects.none())
        if form.is_valid() and formset.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            for option_form in formset:
                if option_form.cleaned_data:
                    option = option_form.save(commit=False)
                    option.poll = poll
                    option.save()
            return redirect('poll_list')
    else:
        form = PollCreationForm()
        formset = OptionFormSet(queryset=PollOption.objects.none())
    return render(request, 'polls/poll_create.html', {'form': form, 'formset': formset})


@login_required
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})


@login_required
def poll_search(request):
    query = request.GET.get('q', '')
    polls = Poll.objects.filter(Q(question__icontains=query) | Q(description__icontains=query))
    return render(request, 'polls/poll_list.html', {'polls': polls, 'query': query})


@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    now = timezone.now()
    if poll.start_date and poll.start_date > now:
        return render(request, 'polls/poll_detail.html', {'poll': poll, 'error': 'Poll not started yet.'})
    if poll.end_date and poll.end_date < now:
        return render(request, 'polls/poll_detail.html', {'poll': poll, 'error': 'Poll has ended.'})

    if request.method == 'POST':
        option_id = request.POST.get('option')
        option = get_object_or_404(PollOption, id=option_id, poll=poll)
        if Vote.objects.filter(poll=poll, voted_by=request.user).exists():
            return render(request, 'polls/poll_detail.html', {'poll': poll, 'error': 'You have already voted.'})
        Vote.objects.create(poll=poll, option=option, voted_by=request.user)
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'polls/poll_detail.html', {'poll': poll})


@login_required
def poll_update(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    # Allow only the poll creator or superuser to update
    if not request.user.is_superuser and poll.created_by != request.user:
        return redirect('poll_detail', poll_id=poll.id)
    OptionFormSet = modelformset_factory(PollOption, form=PollOptionForm, extra=0)
    if request.method == 'POST':
        form = PollCreationForm(request.POST, request.FILES, instance=poll)
        formset = OptionFormSet(request.POST, queryset=poll.options.all())
        if form.is_valid() and formset.is_valid():
            poll = form.save()
            for option_form in formset:
                if option_form.cleaned_data:
                    option = option_form.save(commit=False)
                    option.poll = poll
                    option.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = PollCreationForm(instance=poll)
        formset = OptionFormSet(queryset=poll.options.all())
    return render(request, 'polls/poll_update.html', {'form': form, 'formset': formset, 'poll': poll})


@login_required
def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if not request.user.is_superuser and poll.created_by != request.user:
        return redirect('poll_detail', poll_id=poll.id)
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')
    return render(request, 'polls/poll_delete_confirm.html', {'poll': poll})


@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    options = poll.options.all()
    total_votes = poll.votes.count()
    results = []
    for option in options:
        count = option.votes.count()
        percentage = (count / total_votes * 100) if total_votes > 0 else 0
        results.append({'option': option.option_text, 'votes': count, 'percentage': percentage})
    return render(request, 'polls/poll_results.html', {'poll': poll, 'results': results, 'total_votes': total_votes})


@login_required
def poll_results_json(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    options = poll.options.all()
    total_votes = poll.votes.count()
    data = []
    for option in options:
        count = option.votes.count()
        percentage = (count / total_votes * 100) if total_votes > 0 else 0
        data.append({'option': option.option_text, 'votes': count, 'percentage': percentage})
    return JsonResponse({'results': data, 'total_votes': total_votes})

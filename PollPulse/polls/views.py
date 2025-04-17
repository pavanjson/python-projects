from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Poll, PollOption, Vote
from .forms import RegistrationForm, PollCreationForm, PollOptionForm
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages


otp_storage = {}

def register(request):
    if request.method == 'POST':
        if 'verify_otp' in request.POST:
            email = request.POST.get('email')
            entered_otp = request.POST.get('otp')
            actual_otp = otp_storage.get(email, {}).get('otp')
            user_data = otp_storage.get(email, {}).get('data')

            if entered_otp == actual_otp:
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=email,
                    password=user_data['password']
                )
                del otp_storage[email]
                return redirect('login')
            else:
                return render(request, 'polls/verify_otp.html', {'email': email, 'error': 'Invalid OTP'})

        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            otp = str(random.randint(100000, 999999))
            otp_storage[email] = {
                'otp': otp,
                'data': {
                    'username': form.cleaned_data.get('username'),
                    'password': form.cleaned_data.get('password'),
                }
            }
            # Send email
            send_mail(
                'PollPulse OTP Verification',
                f'Your OTP is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return render(request, 'polls/verify_otp.html', {'email': email})
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

    now = timezone.now()
    polls = Poll.objects.all()

    live_count = polls.filter(start_date__lte=now, end_date__gte=now).count()
    upcoming_count = polls.filter(start_date__gt=now).count()
    past_count = polls.filter(end_date__lt=now).count()
    total_count = polls.count()

    return render(request, 'polls/admin_dashboard.html', {
        'live_count': live_count,
        'upcoming_count': upcoming_count,
        'past_count': past_count,
        'total_count': total_count
    })



def user_dashboard(request):
    polls = Poll.objects.all()  # Optionally filter active polls
    return render(request, 'polls/user_dashboard.html', {'polls': polls})




@login_required
def poll_create(request):
    if not request.user.is_superuser:
        return redirect('poll_list')

    OptionFormSet = modelformset_factory(PollOption, form=PollOptionForm, extra=2, can_delete=True)

    if request.method == 'POST':
        form = PollCreationForm(request.POST, request.FILES)
        formset = OptionFormSet(request.POST, queryset=PollOption.objects.none())
        if form.is_valid() and formset.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            for option_form in formset:
                if option_form.cleaned_data and not option_form.cleaned_data.get('DELETE', False):
                    option = option_form.save(commit=False)
                    option.poll = poll
                    option.save()
            return redirect('poll_list')
    else:
        form = PollCreationForm()
        formset = OptionFormSet(queryset=PollOption.objects.none())

    return render(request, 'polls/poll_create.html', {'form': form, 'formset': formset})



def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})



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

    if request.user.is_superuser:
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'admin_review': True,
            'admin_name': request.user.username
        })

    # Check if user has already voted
    try:
        vote = Vote.objects.get(poll=poll, voted_by=request.user)
        has_voted = True
        voted_option_id = vote.option.id
    except Vote.DoesNotExist:
        has_voted = False
        voted_option_id = None

    if request.method == 'POST':
        if has_voted:
            return render(request, 'polls/poll_detail.html', {
                'poll': poll,
                'error': 'You have already voted.',
                'voted_option_id': voted_option_id,
                'has_voted': True
            })

        option_id = request.POST.get('option')
        if not option_id:
            return render(request, 'polls/poll_detail.html', {
                'poll': poll,
                'error': 'Please select an option to vote.'
            })

        try:
            option = PollOption.objects.get(id=option_id, poll=poll)
        except PollOption.DoesNotExist:
            return render(request, 'polls/poll_detail.html', {
                'poll': poll,
                'error': 'Invalid option selected.'
            })

        Vote.objects.create(poll=poll, option=option, voted_by=request.user)
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'polls/poll_detail.html', {
        'poll': poll,
        'error': 'You have already voted.' if has_voted else None,
        'voted_option_id': voted_option_id,
        'has_voted': has_voted
    })



@login_required
def poll_update(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if not request.user.is_superuser and poll.created_by != request.user:
        return redirect('poll_detail', poll_id=poll.id)

    OptionFormSet = modelformset_factory(PollOption, form=PollOptionForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = PollCreationForm(request.POST, request.FILES, instance=poll)
        formset = OptionFormSet(request.POST, queryset=poll.options.all())

        if form.is_valid() and formset.is_valid():
            # Check for duplicate option texts
            option_texts = [
                opt_form.cleaned_data.get('option_text').strip()
                for opt_form in formset
                if opt_form.cleaned_data and not opt_form.cleaned_data.get('DELETE')
            ]
            if len(option_texts) != len(set(option_texts)):
                messages.error(request, "⚠️ Duplicate options are not allowed.")
            else:
                poll = form.save()

                # Save new/updated options
                options = formset.save(commit=False)
                for option in options:
                    option.poll = poll
                    option.save()

                # Delete removed options
                for deleted_form in formset.deleted_forms:
                    if deleted_form.instance.pk:
                        deleted_form.instance.delete()

                messages.success(request, "✅ Poll updated successfully!")
                return redirect('poll_update', poll_id=poll.id)
        else:
            messages.error(request, "⚠️ Failed to update poll. Please correct the errors below.")

    else:
        form = PollCreationForm(instance=poll)
        formset = OptionFormSet(queryset=poll.options.all())

    return render(request, 'polls/poll_update.html', {
        'form': form,
        'formset': formset,
        'poll': poll,
    })



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
        voters = option.votes.select_related('voted_by').all() if request.user.is_superuser else []
        results.append({
            'option': option.option_text,
            'votes': count,
            'percentage': percentage,
            'voters': voters
        })

    # Data for chart
    chart_labels = [res['option'] for res in results]
    chart_data = [res['votes'] for res in results]

    return render(request, 'polls/poll_results.html', {
        'poll': poll,
        'results': results,
        'total_votes': total_votes,
        'chart_labels': chart_labels,
        'chart_data': chart_data
    })



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

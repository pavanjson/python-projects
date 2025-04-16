from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from .models import Subscriber, Newsletter, NewsletterRecipient, Group
from .forms import SubscriberForm, NewsletterForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'newsletter/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'newsletter/login.html', {'error': 'Invalid credentials'})
    return render(request, 'newsletter/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'newsletter/home.html')


@login_required
def manage_subscribers(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            selected_group = form.cleaned_data['group']
            new_group_name = form.cleaned_data['new_group']

            if new_group_name:
                selected_group, _ = Group.objects.get_or_create(name=new_group_name, user=request.user)

            Subscriber.objects.create(email=email, group=selected_group)
            return redirect('manage_subscribers')
    else:
        form = SubscriberForm()

    # Only show user's subscribers via their groups
    subscribers = Subscriber.objects.filter(group__user=request.user).select_related('group')
    return render(request, 'newsletter/subscribers.html', {
        'form': form,
        'subscribers': subscribers
    })


@login_required
def compose_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            if newsletter.group.user != request.user:
                return redirect('home')
            newsletter.save()

            group = newsletter.group
            subscribers = Subscriber.objects.filter(group=group)

            for sub in subscribers:
                send_mail(
                    newsletter.subject,
                    newsletter.content,
                    'your_email@gmail.com',  # Update this
                    [sub.email]
                )
                NewsletterRecipient.objects.create(newsletter=newsletter, subscriber=sub)

            return redirect('sent_newsletters')
    else:
        form = NewsletterForm()

    # Limit groups in form to current user
    form.fields['group'].queryset = Group.objects.filter(user=request.user)
    return render(request, 'newsletter/compose.html', {'form': form})


@login_required
def sent_newsletters(request):
    newsletters = Newsletter.objects.filter(group__user=request.user).prefetch_related('recipients__subscriber').order_by('-created_at')
    return render(request, 'newsletter/sent_newsletters.html', {'newsletters': newsletters})


@login_required
def group_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Group.objects.get_or_create(name=name, user=request.user)
        return redirect('group_list')

    groups = Group.objects.filter(user=request.user)
    return render(request, 'newsletter/groups.html', {'groups': groups})


@login_required
def delete_group(request, group_id):
    Group.objects.filter(id=group_id, user=request.user).delete()
    return redirect('group_list')


@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id, user=request.user)

    if request.method == 'POST':
        emails = request.POST.get('emails')
        if emails:
            email_list = [e.strip() for e in emails.split(',') if e.strip()]
            for email in email_list:
                Subscriber.objects.get_or_create(email=email, group=group)
        return redirect('group_detail', group_id=group.id)

    subscribers = Subscriber.objects.filter(group=group)
    return render(request, 'newsletter/group_detail.html', {
        'group': group,
        'subscribers': subscribers
    })


@login_required
def delete_subscriber(request, subscriber_id):
    sub = get_object_or_404(Subscriber, id=subscriber_id)
    if sub.group.user != request.user:
        return redirect('group_list')
    group_id = sub.group.id
    sub.delete()
    return redirect('group_detail', group_id=group_id)


@login_required
def newsletter_detail(request, newsletter_id):
    newsletter = get_object_or_404(Newsletter, id=newsletter_id)
    if newsletter.group.user != request.user:
        return redirect('sent_newsletters')

    return render(request, 'newsletter/newsletter_detail.html', {'newsletter': newsletter})

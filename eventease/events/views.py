from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.core.mail import send_mail
from django.db.models import ExpressionWrapper, F, DurationField, DateTimeField
from .forms import EventForm, RSVPForm
from .models import Event, RSVP


# ----------------------------
# Home Page (Public)
# ----------------------------
def home(request):
    return render(request, 'events/home.html')


# ----------------------------
# Dashboard (User’s Events)
# ----------------------------
from django.utils.timezone import now
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event


from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event

from django.db.models import F, ExpressionWrapper, DateTimeField
from django.utils.timezone import now

from django.utils.timezone import now
from django.db.models import ExpressionWrapper, F, DurationField, DateTimeField

from django.db.models import ExpressionWrapper, F, DateTimeField
from django.utils.timezone import now
from .models import Event

from django.utils.timezone import now
from django.db.models import F, ExpressionWrapper, DateTimeField
from .models import Event

@login_required
def dashboard(request):
    current_time = now()

    events = Event.objects.filter(user=request.user).annotate(
        end_time_db=ExpressionWrapper(F('date') + F('duration'), output_field=DateTimeField())
    )

    upcoming_events = events.filter(end_time_db__gte=current_time).order_by('date')
    past_events = events.filter(end_time_db__lt=current_time).order_by('-date')

    return render(request, 'events/dashboard.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })

# ----------------------------
# Create Event
# ----------------------------
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user   # ✅ change user → creator
            event.save()
            messages.success(request, "Event created successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

# ----------------------------
# Edit Event (Only for creator or admin)
# ----------------------------
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user != event.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this event.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please fix the errors.")
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {'form': form})


# ----------------------------
# Event Detail View
# ----------------------------
@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    try:
        existing_rsvp = RSVP.objects.get(event=event, user=request.user)
    except RSVP.DoesNotExist:
        existing_rsvp = None

    if request.method == 'POST':
        form = RSVPForm(request.POST, instance=existing_rsvp)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event
            rsvp.user = request.user
            rsvp.save()
            messages.success(request, "Your RSVP has been submitted.")
            return redirect('event_detail', event_id=event.id)
    else:
        form = RSVPForm(instance=existing_rsvp)

    return render(request, 'events/event_detail.html', {'event': event, 'form': form})


# ----------------------------
# Upcoming Event Reminders
# ----------------------------
@login_required
def reminders(request):
    upcoming_events = Event.objects.filter(user=request.user, date__gte=now()).order_by('date')
    return render(request, 'events/reminders.html', {'upcoming_events': upcoming_events})


# ----------------------------
# RSVP List for Event
# ----------------------------
@login_required
def rsvp_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.user:
        messages.error(request, "Not authorized.")
        return redirect('dashboard')
    rsvps = RSVP.objects.filter(event=event)
    return render(request, 'events/rsvp_list.html', {'event': event, 'rsvps': rsvps})


# ----------------------------
# Send Email Invitation
# ----------------------------
@login_required
def send_invitation_email(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        subject = f"You're invited: {event.title}"
        message = (
            f"You're invited to *{event.title}* 🎉\n\n"
            f"📅 Date: {event.date.strftime('%B %d, %Y – %I:%M %p')}\n"
            f"📍 Location: {event.location}\n\n"
            f"📝 {event.description}\n\n"
            f"Join us via EventEase!\n"
            f"View the event: http://127.0.0.1:8000/event/{event.id}/"
        )
        try:
            send_mail(subject, message, None, [email])
            messages.success(request, f'Invitation sent to {email}')
        except Exception as e:
            messages.error(request, f'Error sending email: {e}')
        return redirect(reverse('event_detail', args=[event.id]))

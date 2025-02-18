from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import Task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@shared_task
def create_recurring_tasks():
    tasks = Task.objects.filter(repeat__in=['daily', 'weekly', 'monthly'], completed=False)
    for task in tasks:
        if task.repeat == 'daily':
            next_due = now() + timedelta(days=1)
        elif task.repeat == 'weekly':
            next_due = now() + timedelta(weeks=1)
        elif task.repeat == 'monthly':
            next_due = now() + timedelta(weeks=4)

        Task.objects.create(
            user=task.user,
            title=task.title,
            description=task.description,
            priority=task.priority,
            due_date=next_due,
            repeat=task.repeat
        )



@shared_task
def send_task_notifications():
    channel_layer = get_channel_layer()
    tasks = Task.objects.filter(due_date__date=now().date(), completed=False)

    for task in tasks:
        message = f"Reminder: '{task.title}' is due today!"
        async_to_sync(channel_layer.group_send)(
            "task_notifications_group",
            {"type": "send_task_notification", "message": message}
        )

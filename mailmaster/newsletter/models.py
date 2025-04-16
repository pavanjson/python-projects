from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='subscribers')

    class Meta:
        unique_together = ('email', 'group')

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class NewsletterRecipient(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='recipients')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscriber.email} received {self.newsletter.subject}"

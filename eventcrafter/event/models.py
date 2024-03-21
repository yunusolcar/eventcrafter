from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to='events')
    slug = models.SlugField(null=False, unique=True, db_index=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events', db_index=True)
    participants = models.ManyToManyField(User, related_name='joined_events')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Notification(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    recipients = models.ManyToManyField(User, related_name='received_notifications')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class Comment(models.Model):
    text = models.TextField(max_length=500)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.name}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed_user')

    def __str__(self):
        return f'{self.follower.username} follows {self.followed_user.username}'

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    is_interested = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(null=False, unique=True, db_index=True)
    participants = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Notification(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField()

    def __str__(self):
        return f"{self.participants.username} - {self.event.name}"

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class Comment(models.Model):
    text = models.TextField(max_length=500)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    participants = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

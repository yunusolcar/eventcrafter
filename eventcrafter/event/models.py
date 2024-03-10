from django.db import models
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    is_interested = models.BooleanField(default=False)
    member = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name



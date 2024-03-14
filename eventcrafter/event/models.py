from django.db import models
from django.utils.text import slugify


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    is_interested = models.BooleanField(default=False)
    member = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

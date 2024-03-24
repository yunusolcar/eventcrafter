from django.contrib import admin
from .models import Event, Notification, Comment


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'slug')
    search_fields = ('name', 'member')
    readonly_fields = ('slug',)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('event', 'message')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'event', 'user')


admin.site.register(Event, EventAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Comment, CommentAdmin)

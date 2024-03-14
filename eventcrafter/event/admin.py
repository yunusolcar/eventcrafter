from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'is_interested', 'created_at', 'slug')
    list_editable = ('is_interested',)
    search_fields = ('name', 'member')
    readonly_fields = ('slug',)

admin.site.register(Event, EventAdmin)
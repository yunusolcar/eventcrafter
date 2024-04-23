from django import forms
from django.forms import widgets
from event.models import Event, Comment


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'event_date', 'location']

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.FileInput(attrs={'class': 'form-control'}),
            'event_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'creator': widgets.HiddenInput(),
        }


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': widgets.Textarea(attrs={'class': 'form-control', }),
        }

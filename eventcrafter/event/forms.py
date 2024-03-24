from django import forms
from django.forms import widgets
from event.models import Event


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'event_date', 'participants']
        error_messages = {
            'name': {
                'required': 'Name is required!',
                'max_length': 'Max 100 characters, please!'
            }
        }

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'image': widgets.FileInput(),
            'event_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'participants': widgets.SelectMultiple(attrs={'class': 'form-control'}),
            'creator': widgets.HiddenInput(),
        }

from django.shortcuts import render, redirect
from event.models import Event
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import CreateEventForm
from django.urls import reverse
import pdb


# Create your views here.
def index(request):
    events = Event.objects.all()
    participant_count = User.objects.all().count()
    event_count = Event.objects.all().count()
    context = {
        'events': events,
        'participant_count': participant_count,
        'event_count': event_count
    }

    return render(request, 'event/index.html', context)


def events(request):
    context = {'events': Event.objects.all()}
    return render(request, 'event/events.html', context)


def single_event(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'event/single-event.html', {"event": event})


def about(request):
    return render(request, 'event/about.html')


class CreateEvent(View):

    def get(self, request):
        # pdb.set_trace()
        form = CreateEventForm()
        return render(request, 'event/create-event.html', {'form': form})

    def post(self, request):
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            print(request.user)
            return redirect('create-event')
        else:
            print(form.errors)
            return render(request, 'event/create-event.html', {'form': form})

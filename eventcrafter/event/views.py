from django.shortcuts import render
from event.models import Event
from django.contrib.auth.models import User


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


def create_event(request):
    return render(request, 'event/create-event.html')

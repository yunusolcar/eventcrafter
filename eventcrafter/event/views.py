from django.shortcuts import render, redirect
from event.models import Event
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import CreateEventForm
from django.utils import timezone


# Create your views here.
def index(request):
    now = timezone.now()
    events = Event.objects.filter(event_date__gte=now).order_by('event_date')[:3]
    participant_count = User.objects.all().count()
    event_count = Event.objects.all().count()
    context = {
        'events': events,
        'participant_count': participant_count,
        'event_count': event_count
    }

    return render(request, 'event/index.html', context)


def events(request):
    now = timezone.now()
    events = Event.objects.filter(event_date__gte=now).order_by('event_date')[:12]
    context = {
        'events': events}
    return render(request, 'event/events.html', context)


def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'event/event-detail.html', {"event": event})


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
            return redirect('create-event')
        else:
            return render(request, 'event/create-event.html', {'form': form})

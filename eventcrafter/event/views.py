from django.shortcuts import render
from event.models import Event
from .forms import EventForm
# Create your views here.
def index(request):
    context = {'events': Event.objects.all()}
    return render(request,'event/index.html', context)

def events(request):
    context = {'events': Event.objects.all()}
    return render(request, 'event/events.html', context)

def single_event(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'event/single-event.html', {"event":event})

def create_event(request):
    if request.method == 'POST':
        form

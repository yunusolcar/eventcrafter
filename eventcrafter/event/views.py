from django.shortcuts import render
from event.models import Event
# Create your views here.
def index(request):
    context = {'events': Event.objects.all()}
    return render(request,'event/index.html', context)

def events(request):
    context = {'events': Event.objects.all()}
    return render(request, 'event/events.html', context)

def single_event(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event/single-event.html', {"event":event})
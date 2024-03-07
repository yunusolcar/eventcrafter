from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'event/index.html')

def events(request):
    return render(request, 'event/events.html')

def single_event(request, id):
    return render(request, 'event/single-event.html', {"id":id})
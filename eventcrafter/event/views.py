from django.shortcuts import render, redirect, get_object_or_404
from event.models import Event, Comment
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import CreateEventForm, CreateCommentForm
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login')
def index(request):
    now = timezone.now()
    events = Event.objects.filter(event_date__gte=now).order_by('event_date')[:3]
    participant_count = User.objects.count()
    event_count = Event.objects.count()
    context = {
        'events': events,
        'participant_count': participant_count,
        'event_count': event_count
    }

    return render(request, 'event/index.html', context)


@login_required(login_url='/account/login')
def events(request):
    now = timezone.now()
    events = Event.objects.filter(event_date__gte=now).order_by('event_date')[:12]
    context = {
        'events': events}
    return render(request, 'event/events.html', context)


class CommentView(View):
    def get(self, request, slug):
        event = Event.objects.get(slug=slug)
        comments = Comment.objects.filter(event=event)
        form = CreateCommentForm()
        context = {
            'event': event,
            'comments': comments,
            'form': form
        }
        return render(request, 'event/event-detail.html', context)

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.event = event
            comment.save()
            return redirect('events')
        else:
            context = {
                'event': event,
                'form': form
            }
            return render(request, 'event/event-detail.html', context)


@login_required(login_url='/account/login')
def about(request):
    participant_count = User.objects.count()
    event_count = Event.objects.count()
    context = {
        'events': events,
        'participant_count': participant_count,
        'event_count': event_count
    }
    return render(request, 'event/about.html', context)


class CreateEvent(View):
    def get(self, request):
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


@login_required(login_url='/account/login')
def joined_events(request, slug):
    event = get_object_or_404(Event, slug=slug)

    if request.method == "POST":
        event.participants.add(request.user)
        return redirect('event-detail', slug=slug)
    else:
        return redirect('about')


@login_required(login_url='/account/login')
def leaved_events(request, slug):
    event = get_object_or_404(Event, slug=slug)

    if request.method == "POST":
        event.participants.remove(request.user)
        return redirect('event-detail', slug=slug)
    else:
        return redirect('about')


class Autocomplete(View):

    def get(self, request):
        query = request.GET.get('term', '')
        events = Event.objects.filter(slug__icontains=query)[:3]
        data = [{'id': event.id, 'name': event.name, 'slug': event.slug} for event in events]
        return JsonResponse(data, safe=False)

from django.urls import path
from . import views
from .views import CreateEvent

urlpatterns = [
    path("", views.index, name='index'),
    path("events", views.events, name='events'),
    path("events/<slug:slug>", views.event_detail, name='event-detail'),
    path("about", views.about, name='about'),
    path("create-event", CreateEvent.as_view(), name='create-event')
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("events", views.events, name='events'),
    path("events/<slug:slug>", views.single_event, name='single-event')
]
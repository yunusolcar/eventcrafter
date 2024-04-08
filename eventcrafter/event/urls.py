from django.urls import path
from . import views
from .views import CreateEvent, CommentView, Autocomplete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<slug:slug>', login_required(CommentView.as_view(), login_url='/account/login'), name='event-detail'),
    path('about', views.about, name='about'),
    path('create-event', login_required(CreateEvent.as_view(), login_url='/account/login'), name='create-event'),
    path('join/<slug:slug>', views.joined_events, name='joined_events'),
    path('leave/<slug:slug>', views.leaved_events, name='leaved_events'),
    path('autocomplete/', Autocomplete.as_view(), name='autocomplete'),
]

from django.urls import path
from . import views
from .views import CreateEvent, CommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<slug:slug>', CommentView.as_view(), name='event-detail'),
    path('about', views.about, name='about'),
    path('create-event', CreateEvent.as_view(), name='create-event'),
    path('join/<slug:slug>', views.joined_events, name='joined_events'),
    path('leave/<slug:slug>', views.leaved_events, name='leaved_events')
]

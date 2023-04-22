from django.contrib.auth.decorators import login_required
from django.urls import path

import events.views

app_name = 'events'
urlpatterns = [
    path('', events.views.EventsListView.as_view(), name='events_list'),
    path(
        'create/',
        login_required(events.views.EventCreateView.as_view()),
        name='create_event',
    ),
    path(
        'ajax/offline_events',
        events.views.get_ajax_all_events,
        name='ajax_offline_events',
    ),
    path(
        'add_members/',
        login_required(events.views.EventsListView.as_view()),
        name='add_members',
    ),
    path(
        '<int:id>/',
        events.views.EventDetail.as_view(),
        name='detail',
    ),
]

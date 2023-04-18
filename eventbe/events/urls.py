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
    path('ajax/all_events', events.views.get_ajax_all_events),
    path(
        'update/',
        login_required(events.views.EventUpdateView.as_view()),
        name='update_event',
    ),
]

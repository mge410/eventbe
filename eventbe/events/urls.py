from django.urls import path

import events.views

app_name = 'events'
urlpatterns = [
    path('', events.views.EventsListView.as_view(), name='events_list'),
]

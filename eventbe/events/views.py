import django.db.models
import django.views.generic

import events.models


class EventListView(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.order_by(
        events.models.Event.date,
    ).only(
        events.models.Event.events.models.Event.organizer,
    )

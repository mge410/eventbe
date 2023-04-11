import django.db.models
import django.urls
import django.views.generic

import events.forms
import events.models


class EventListView(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.order_by(
        events.models.Event.date,
    ).only(
        events.models.Event.events.models.Event.organizer,
    )


class EventCreateView(django.views.generic.CreateView):
    template_name = 'events/create_event.html'
    model = events.models.Event
    form_class = events.forms.EventCrUpdForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs) -> str:
        return django.urls.reverse('event:successfullycreated')


class EventUpdateView(django.views.generic.UpdateView):
    template_name = 'events/update_event.html'
    model = events.models.Event
    form_class = events.forms.EventCrUpdForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs) -> str:
        return django.urls.reverse('event:successfullycreated')

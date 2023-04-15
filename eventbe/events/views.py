import django.contrib.messages as messages
import django.db.models
import django.urls
import django.views.generic

import events.forms
import events.models


class EventsListView(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_list()


class EventsSortedByDateView(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_new_to_old()


class EventsOnline(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_online()


class EventsOffline(django.views.generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_offline()


class EventDetail(django.views.generic.DetailView):
    model = events.models.Event
    template_name = 'events/event_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'event'


class EventCreateView(django.views.generic.CreateView):
    template_name = 'events/create_event.html'
    model = events.models.Event
    form_class = events.forms.EventCreateUpdateForm

    def form_valid(self, form):
        creator = self.request.user
        event = form.save(commit=False)
        event.organizer = creator
        event.save()
        # send mail
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs) -> str:
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The event is successfully created',
        )
        return django.urls.reverse('events:events_list')


class EventUpdateView(django.views.generic.UpdateView):
    template_name = 'events/update_event.html'
    model = events.models.Event
    form_class = events.forms.EventCreateUpdateForm

    def form_valid(self, form):
        form.save()
        # send mail
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs) -> str:
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The event is successfully updated',
        )
        return django.urls.reverse('events:events_list')

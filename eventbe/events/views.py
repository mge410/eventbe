import django.contrib.messages as messages
import django.db.models
import django.urls
import django.views.generic
import django.core.paginator
import events.filters
import events.forms
import events.models
import django.shortcuts


class EventsListView(django.views.generic.View):
    template_name = 'events/events_list.html'

    def get(self, request):
        context = {
            'filter': events.filters.ProductFilter(
                self.request.GET,
                queryset=events.models.Event.objects.events_list(),
            )
        }
        paginator = django.core.paginator.Paginator(context['filter'].qs, per_page=9)
        context['page_obj'] = paginator.get_page(request.GET.get('page', 1))
        return django.shortcuts.render(request, self.template_name, context)


class EventsSortedByDateView(django.views.generic.ListView):
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_new_to_old()


class EventsOnline(django.views.generic.ListView):
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    queryset = events.models.Event.objects.events_online()


class EventsOffline(django.views.generic.ListView):
    template_name = 'events/events_list.html'
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

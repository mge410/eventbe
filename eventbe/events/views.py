import django.contrib.messages as messages
import django.core.paginator
import django.core.serializers
import django.db.models
import django.http
import django.shortcuts
import django.urls
import django.views.generic

import events.filters
import events.forms
import events.models


class EventsListView(django.views.generic.View):
    template_name = 'events/events_list.html'

    def get(self, request):
        context = {
            'filter': events.filters.ProductFilter(
                self.request.GET,
                queryset=events.models.Event.objects.events_list(),
            )
        }
        paginator = django.core.paginator.Paginator(
            context['filter'].qs, per_page=9
        )
        context['page_obj'] = paginator.get_page(request.GET.get('page', 1))
        return django.shortcuts.render(request, self.template_name, context)


class EventDetail(
    django.views.generic.edit.FormMixin, django.views.generic.DetailView
):
    model = events.models.Event
    form_model = events.models.EventComment
    template_name = 'events/event_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'event'
    form_class = events.forms.EventCommentForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context[
            'comments'
        ] = events.models.EventComment.objects.comments_by_event_id(
            self.kwargs['id']
        )
        return context

    def get_success_url(self, **kwargs):
        return django.urls.reverse_lazy(
            'events:detail',
            kwargs={'id': kwargs['id']},
        )

    def post(
        self,
        request: django.http.HttpRequest,
        *args,
        **kwargs,
    ) -> django.http.HttpResponse:
        form = self.form_class(request.POST or None)
        current_user = request.user
        current_event_id = kwargs.get('id')
        current_event = self.model.objects.get(id=current_event_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            comment.event = current_event
            comment.save()
        return django.shortcuts.redirect(self.get_success_url(**self.kwargs))


class EventCreateView(django.views.generic.CreateView):
    template_name = 'events/create_event.html'
    model = events.models.Event
    form_class = events.forms.EventCreateForm

    def form_valid(self, form):
        creator = self.request.user
        event = form.save(commit=False)
        event.organizer = creator
        event.save()
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
    form_class = events.forms.EventUpdateForm
    thumbnail_form_class = events.forms.EventThumbnailUpdateForm
    gallery_form_class = events.forms.EventGalleryUpdateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs) -> dict:
        event = self.get_object()

        context = super().get_context_data(**kwargs)
        context['thumbnail_form'] = self.thumbnail_form_class(
            instance=event.thumbnail,
        )
        context['gallery_form'] = self.gallery_form_class(
            instance=event.gallery,
        )

    def form_valid(self, form) -> django.http.HttpResponse:
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs) -> None:
        event = self.get_object()

        event_dataform = events.forms.EventUpdateForm(
            request.POST, instance=event
        )
        event_thumbnailform = events.forms.EventThumbnailUpdateForm(
            request.POST,
            request.FILES,
            instance=event.thumbnail,
        )

        if event_dataform.is_valid() and event_thumbnailform.is_valid():
            event_dataform.save()
            event_thumbnailform.save()
        return django.urls.reverse('events:detail', kwargs={'id': event.id})

    def get_success_url(self, *args, **kwargs) -> str:
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The event is successfully updated',
        )
        return django.urls.reverse('events:events_list')


def get_ajax_all_events(request):
    events_objects = events.models.Event.objects.offline_events()
    response = {'events': [model for model in events_objects]}
    return django.http.JsonResponse(response)

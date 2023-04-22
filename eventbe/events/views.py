import django.contrib.messages as messages
import django.core.mail
import django.core.paginator
import django.core.serializers
import django.db.models
import django.http
from django.http import HttpResponseRedirect
import django.shortcuts
import django.urls
from django.urls import reverse_lazy
import django.views.generic
from django.views.generic import FormView

import events.filters
import events.forms
import events.models
import users.models


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

    def get_success_url(self, **kwargs):
        return django.urls.reverse_lazy(
            'events:detail',
            kwargs={'id': kwargs['id']},
        )

    def post(self, request: django.http.HttpRequest, *args, **kwargs):
        user = users.models.User.objects.get(id=request.user.id)
        event = events.models.Event.objects.get(id=request.POST['event_id'])
        if request.user in event.members.all():
            event.members.remove(request.user)
            event.organizer.coins -= 10
            user.events_organized -= 1
            user.events_visited -= 1
            user.coins -= 10
            messages.success(
                self.request, 'You are no longer a participant of the event!'
            )
        else:
            event.members.add(request.user)
            event.organizer.coins += 10
            user.events_organized += 1
            user.events_visited += 1
            user.coins += 10
            messages.success(self.request, 'You are an event participant!')
        user.save()
        event.organizer.save()
        return django.shortcuts.redirect(self.get_success_url(**{'id': 1}))


class EventDetail(
    django.views.generic.DetailView, django.views.generic.edit.FormMixin
):
    model = events.models.Event
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
        context['users'] = users.models.User.objects.all()
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
        current_event_id = kwargs.get('id')
        current_event = self.model.objects.get(id=current_event_id)
        if 'delete_event' in request.POST:
            current_event.delete()
            messages.success(
                request,
                'The event has been successfully deleted',
            )
            return django.shortcuts.redirect(
                'events:user_events',
            )

        form = self.form_class(request.POST or None)
        current_user = request.user
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            comment.event = current_event
            comment.save()
        return django.shortcuts.redirect(self.get_success_url(**self.kwargs))


class EventCreateView(django.views.generic.CreateView):
    template_name = 'events/create_event.html'
    model = events.models.Event
    form_class = events.forms.EventForm
    second_form_class = events.forms.EventThumbnailForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['thumbnail_form'] = self.second_form_class()
        if self.request.POST:
            context['thumbnail_form'] = self.second_form_class(
                self.request.POST, self.request.FILES
            )
        else:
            context['thumbnail_form'] = self.second_form_class()
        return context

    def form_valid(self, form):
        print(self.request.FILES)
        context = self.get_context_data()
        creator = self.request.user
        event = form.save(commit=False)
        event.organizer = creator
        event.save()
        thumbnail_form = context['thumbnail_form']
        event_image = thumbnail_form.save(commit=False)
        event_image.event = event
        event_image.save()
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
    form_class = events.forms.EventForm
    pk_url_kwarg = 'id'
    context_object_name = 'event'

    def get_success_url(self, *args, **kwargs) -> str:
        return django.urls.reverse_lazy(
            'events:detail',
            kwargs={'id': self.get_object().id},
        )

    def form_valid(self, form) -> django.http.HttpResponse:
        event = form.save(commit=False)
        event.is_published = False
        event.save()
        return super().form_valid(form)


class EventsUserList(django.views.generic.View):
    template_name = 'events/events_list.html'

    def get(self, request):
        context = {
            'filter': events.filters.ProductFilter(
                self.request.GET,
                queryset=events.models.Event.objects.user_created_events(
                    self.request.user.id
                ),
            ),
        }
        paginator = django.core.paginator.Paginator(
            context['filter'].qs, per_page=9
        )
        context['page_obj'] = paginator.get_page(request.GET.get('page', 1))
        return django.shortcuts.render(request, self.template_name, context)


class TagCreateView(FormView):
    form_class = events.forms.AddTags
    template_name = 'events/add_tags.html'
    success_url = reverse_lazy('events:create_tags')

    def form_valid(self, form: events.forms.AddTags) -> HttpResponseRedirect:
        form.save()
        messages.success(self.request, 'Thanks for the application')
        return super().form_valid(form)


def get_ajax_all_events(request):
    events_objects = events.models.Event.objects.offline_events()
    response = {'events': [model for model in events_objects]}
    return django.http.JsonResponse(response)

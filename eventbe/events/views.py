from django.views.generic import TemplateView


class EventsListView(TemplateView):
    template_name = 'layouts/base.html'

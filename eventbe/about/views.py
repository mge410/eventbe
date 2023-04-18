import django.views.generic.base


class AboutView(django.views.generic.base.TemplateView):
    template_name = 'about/about.html'

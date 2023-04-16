from django.conf import settings
from django.contrib import messages
import django.core.mail as mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

import feedback.forms as forms


class FeedbackView(FormView):
    form_class = forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form: forms.FeedbackForm) -> HttpResponseRedirect:
        form.save()
        try:
            mail.send_mail(
                'Feedback',
                f'Thanks for the feedback <br> Your message '
                f'- « {form.cleaned_data["text"]} »',
                settings.MAIL_SENDER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            messages.success(self.request, 'Thank you for your feedback')
        except Exception:
            messages.error(
                self.request,
                'An unknown error occurred, try again later',
            )
        return super().form_valid(form)

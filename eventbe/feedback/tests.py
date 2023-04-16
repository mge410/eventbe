from django.test import Client
from django.test import TestCase
import django.urls

import feedback.forms as forms
import feedback.models as models


class FeedbackFormTests(TestCase):
    def setUp(self) -> None:
        self.feedback_form = forms.FeedbackForm()
        super(FeedbackFormTests, self).setUp()

    def test_text_label(self) -> None:
        text_label = self.feedback_form['text'].label
        self.assertEquals(text_label, 'Message *')

    def test_email_label(self) -> None:
        email_label = self.feedback_form['email'].label
        self.assertEquals(email_label, 'Email *')

    def test_text_help_text(self) -> None:
        text_help_text = self.feedback_form['text'].help_text
        self.assertEquals(text_help_text, 'Feedback message')

    def test_email_help_text(self) -> None:
        email_help_text = self.feedback_form.fields['email'].help_text
        self.assertEquals(email_help_text, 'Your email address')


class FeedbackViewTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.form = forms.FeedbackForm()

    def test_feedback_context(self) -> None:
        response = Client().get(
            django.urls.reverse(
                'feedback:feedback',
            )
        )
        self.assertIn('form', response.context)

    def test_feedback_success_save(self) -> None:
        feedback_count = models.Feedback.objects.count()
        form_data = {
            'email': 'fff@mail.com',
            'text': '123123',
        }

        Client().post(
            django.urls.reverse(
                'feedback:feedback',
            ),
            data=form_data,
        )

        self.assertEqual(models.Feedback.objects.count(), feedback_count + 1)

    def test_feedback_error_save(self) -> None:
        feedback_count = models.Feedback.objects.count()
        form_data = {
            'email': 'fffmail.com',
            'text': '123123',
        }

        Client().post(
            django.urls.reverse(
                'feedback:feedback',
            ),
            data=form_data,
        )

        self.assertEqual(models.Feedback.objects.count(), feedback_count)

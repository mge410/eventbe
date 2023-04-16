import django.db.models
from django.utils.translation import ugettext_lazy as _


class Feedback(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        accepted = 'c', 'accepted'
        processed = 'b', 'processed'
        replied = 'a', 'replied'

    text = django.db.models.TextField(
        _('message *'),
        max_length=200,
        blank=False,
        help_text=_('Feedback message'),
    )

    email = django.db.models.EmailField(
        _('email *'),
        max_length=254,
        help_text=_('Your email address'),
    )

    created_at = django.db.models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )

    status = django.db.models.CharField(
        _('status'),
        max_length=2,
        default=Status.accepted,
        choices=Status.choices,
        help_text='Feedback status',
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'

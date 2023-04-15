import django.db.models
from django.utils.translation import ugettext_lazy as _

import users.models


class Feedback(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        accepted = 'c', 'accepted'
        processed = 'b', 'processed'
        replied = 'a', 'replied'

    text = django.db.models.TextField(
        _('text field'),
        max_length=200,
        blank=False,
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

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('feedback author'),
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'

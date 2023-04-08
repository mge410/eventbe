import django.db.models
from django.utils.translation import ugettext_lazy as _

import users.models


class Tag(django.db.models.Model):
    title = django.db.models.CharField(
        _('title'),
        max_length=20,
        blank=False,
    )
    slug = django.db.models.SlugField(
        _('slug'),
        blank=False,
    )
    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )
    is_active = django.db.models.BooleanField(
        _('is active'),
        default=True,
    )


class Event(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        public = 'pub', 'public'
        authorizedonly = 'authonly', 'authorized_only'
        private = 'priv', 'private'

    title = django.db.models.CharField(
        _('title'),
        max_length=40,
        blank=False,
    )
    description = django.db.models.TextField(
        _('description'),
        max_length=300,
        blank=False,
    )
    datetime = django.db.models.DateTimeField(
        _('date & time'),
        blank=False,
    )
    location_x = django.db.models.FloatField(
        _('location x'),
        null=True,
    )
    location_y = django.db.models.FloatField(
        _('location y'),
        null=True,
    )
    status = django.db.models.CharField(
        _('status'),
        default=Status.public,
        choices=Status.choices,
        help_text=_('Event Status'),
        max_length=8,
    )
    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )
    is_offline = django.db.models.BooleanField(
        _('is offline'),
        default=False,
    )
    is_active = django.db.models.BooleanField(
        _('is active'),
        default=True,
    )
    is_published = django.db.models.BooleanField(
        _('is published'),
        default=True,
    )
    is_frozen = django.db.models.BooleanField(
        _('is frozen'),
        default=False,
    )

    tags = django.db.models.ManyToManyField(
        Tag,
        verbose_name='tags',
        help_text='Event must have at least 1 tag',
    )

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('event author'),
    )

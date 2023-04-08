import django.db.models
from django.utils.translation import ugettext_lazy as _


class Tag(django.db.models.Model):
    title = django.db.models.CharField(
        _('title'), max_length=20, blank=False, verbose_name='Tag title'
    )
    slug = django.db.models.SlugField(
        _('slug'), blank=False, verbose_name='Tag slug'
    )
    created_at = django.db.models.DateField(
        _('created at'), auto_now_add=True, verbose_name='Tag created at'
    )
    is_active = django.db.models.BooleanField(
        _('is active'), default=True, verbose_name='Tag is active'
    )


class Event(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        public = 'pub', 'public'
        authorizedonly = 'authonly', 'authorized_only'
        private = 'priv', 'private'

    title = django.db.models.CharField(
        _('title'), max_length=40, blank=False, verbose_name='Event title'
    )
    description = django.db.models.TextField(
        _('description'), blank=False, verbose_name='Event description'
    )
    datetime = django.db.models.DateTimeField(
        _('date & time'), blank=False, verbose_name='Event date & time'
    )
    location_x = django.db.models.FloatField(
        _('location x'), null=True, verbose_name='Event location_x'
    )
    location_y = django.db.models.FloatField(
        _('location y'), null=True, verbose_name='Event location_y'
    )
    status = django.db.models.CharField(
        _('status'),
        default=Status.public,
        choices=Status.choices,
        help_text=_('Event Status'),
        max_length=8,
        verbose_name='Event status',
    )
    created_at = django.db.models.DateField(
        _('created at'), auto_now_add=True, verbose_name='Event created at'
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

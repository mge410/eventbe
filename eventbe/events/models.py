import django.db.models
import django.utils.html
from django.utils.translation import ugettext_lazy as _

import core.models
import events.managers
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
        default='000_000',
    )
    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )
    is_active = django.db.models.BooleanField(
        _('is active'),
        default=True,
    )

    def __str__(self) -> str:
        return self.title[:20]


class Event(django.db.models.Model):
    objects = events.managers.EventManager()

    class Status(django.db.models.TextChoices):
        public = 'pub', 'public'
        authorizedonly = 'authonly', 'authorized only'
        private = 'priv', 'private'

    title = django.db.models.CharField(
        _('title'),
        max_length=40,
        blank=False,
        help_text=_('Provide a title for your event'),
    )
    description = django.db.models.TextField(
        _('description'),
        max_length=300,
        blank=False,
        help_text=_('Describe your event'),
    )
    date = django.db.models.DateTimeField(
        _('date & time'),
        blank=False,
        help_text=_('Set date & time for your event'),
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
        max_length=8,
        help_text=_('Set status for your event'),
    )
    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )
    is_offline = django.db.models.BooleanField(
        _('is offline'),
        default=False,
        help_text=_('Click if the event is offline'),
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
        to=Tag,
        related_name='tags',
        help_text=_('Select appropriate tags for your event'),
    )

    organizer = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('organizer'),
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self) -> str:
        return self.title[:30]


class EventThumbnail(core.models.ImageModel):
    def saving_path(self, name):
        return f'uploads/events/{self.event.id}/{name}'

    event = django.db.models.OneToOneField(
        to=Event,
        verbose_name='main image',
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
        help_text='main image',
    )

    image = django.db.models.ImageField(
        'image',
        upload_to=saving_path,
        help_text='Will be rendered at 300px',
    )

    class Meta:
        verbose_name = 'event image'
        verbose_name_plural = 'event images'
        default_related_name = 'event_image'


class EventGallery(core.models.ImageModel):
    def saving_path(self, name):
        return f'uploads/gallery_images/{self.event.id}/{name}'

    image = django.db.models.ImageField(
        'image',
        upload_to=saving_path,
        help_text=_('Will be rendered at 300x300 px'),
    )

    event = django.db.models.ForeignKey(
        Event,
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
        verbose_name='gallery images',
        help_text=_('gallery images'),
    )

    class Meta:
        verbose_name = 'Event Gallery Photo'
        verbose_name_plural = 'Event Gallery Photos'
        default_related_name = 'gallery_images'


class EventComment(django.db.models.Model):
    objects = events.managers.EventCommentManager()

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        help_text=_('Comment author'),
    )

    message = django.db.models.TextField(
        _('comment'),
        max_length=100,
        blank=False,
        null=False,
        help_text=_('Your comment'),
    )

    event = django.db.models.ForeignKey(
        Event,
        on_delete=django.db.models.CASCADE,
        verbose_name='comment',
        help_text=_('commented event'),
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        default_related_name = 'comments'

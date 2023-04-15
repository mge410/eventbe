import typing as tp

import django.db.models
import django.utils.html
from django.utils.translation import ugettext_lazy as _
import sorl.thumbnail

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
    )
    description = django.db.models.TextField(
        _('description'),
        max_length=300,
        blank=False,
    )
    date = django.db.models.DateTimeField(
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

    tags = django.db.models.ManyToManyField(Tag)

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
        return f'uploads/eventthumbnail/{self.events.id}/{name}'

    events = django.db.models.OneToOneField(
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

    def get_image_300x300(self) -> tp.Any:
        return sorl.thumbnail.get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )

    def image_tmb(self) -> tp.AnyStr:
        if self.image:
            return django.utils.html.mark_safe(
                f'<img src="{self.get_image_300x300().url}">',
            )
        return 'No picture'

    image_tmb.short_description = 'image'


class EventGallery(core.models.ImageModel):
    gallery_images = django.db.models.ForeignKey(
        to=Event,
        on_delete=django.db.models.CASCADE,
        related_name='event_gallery',
        default=None,
        null=True,
    )

    class Meta:
        verbose_name = 'Event Gallery Photo'
        verbose_name_plural = 'Event Gallery Photos'
        default_related_name = 'event_gallery'


class EventComment(django.db.models.Model):
    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        help_text=_('comment author'),
    )

    message = django.db.models.TextField(
        _('comment'),
        max_length=100,
        blank=False,
        null=False,
        help_text=_('Write the comment here'),
    )

    event = django.db.models.ForeignKey(
        Event,
        on_delete=django.db.models.CASCADE,
        verbose_name='comment',
        help_text=_('comment'),
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        default_related_name = 'comments'

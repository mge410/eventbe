from django.core.exceptions import ValidationError
import django.db.models
import django.utils.html
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

import core.models
import events.managers
import users.models


def validate_image_size(image):
    file_size = image.file.size
    limit_mb = 8
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f'Max size of file is {limit_mb} MB')


class Tag(django.db.models.Model):
    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )

    is_active = django.db.models.BooleanField(
        _('is active'),
        default=True,
    )

    slug = django.db.models.SlugField(
        _('slug'),
        blank=False,
        unique=True,
        default='000_000',
        help_text=_('tag slug'),
    )

    title = django.db.models.CharField(
        _('title'),
        max_length=20,
        unique=True,
        blank=False,
        help_text=_('tag title'),
    )

    def __str__(self) -> str:
        return self.title[:15]


class Event(django.db.models.Model):
    objects = events.managers.EventManager()

    class Status(django.db.models.TextChoices):
        public = 'pub', 'public'
        authorizedonly = 'authonly', 'authorized only'
        private = 'priv', 'private'

    created_at = django.db.models.DateField(
        _('created at'),
        auto_now_add=True,
    )

    date = django.db.models.DateTimeField(
        _('date & time'),
        blank=False,
        help_text=_('format: yyyy-mm-dd hh:mm'),
    )

    description = HTMLField(
        _('description'),
        max_length=300,
        blank=False,
        help_text=_('Describe your event'),
    )

    title = django.db.models.CharField(
        _('title'),
        max_length=40,
        blank=False,
        help_text=_('Provide a title for your event'),
    )

    is_active = django.db.models.BooleanField(
        _('is active'),
        default=True,
    )

    is_frozen = django.db.models.BooleanField(
        _('is frozen'),
        default=False,
    )

    is_offline = django.db.models.BooleanField(
        _('is offline'),
        default=False,
    )

    is_published = django.db.models.BooleanField(
        _('is published'),
        default=True,
    )

    location_x = django.db.models.FloatField(
        _('location x'),
        null=True,
    )

    location_y = django.db.models.FloatField(
        _('location y'),
        null=True,
    )

    organizer = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('organizer'),
    )

    status = django.db.models.CharField(
        _('status'),
        default=Status.public,
        choices=Status.choices,
        max_length=8,
        help_text=_('Set status for your event'),
    )

    tags = django.db.models.ManyToManyField(
        to=Tag,
        related_name='tags',
        help_text=_('Select appropriate tags for your event'),
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self) -> str:
        return self.title[:30]


class EventComment(django.db.models.Model):
    objects = events.managers.EventCommentManager()

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        help_text=_('Comment author'),
    )

    event = django.db.models.ForeignKey(
        Event,
        on_delete=django.db.models.CASCADE,
        verbose_name='comment',
        help_text=_('commented event'),
    )

    message = django.db.models.TextField(
        _('comment'),
        max_length=100,
        blank=False,
        null=False,
        help_text=_('Your comment'),
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        default_related_name = 'comments'


class EventGallery(core.models.ImageModel):
    def saving_path(self, name):
        return f'uploads/gallery_images/{self.event.id}/{name}'

    event = django.db.models.ForeignKey(
        Event,
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('gallery images'),
        help_text=_('gallery images'),
    )

    image = django.db.models.ImageField(
        'image',
        upload_to=saving_path,
        help_text=_('Will be rendered at 300x300 px'),
        validators=[validate_image_size],
    )

    class Meta:
        verbose_name = 'Event Gallery Photo'
        verbose_name_plural = 'Event Gallery Photos'
        default_related_name = 'gallery_images'


class EventThumbnail(core.models.ImageModel):
    def saving_path(self, name):
        return f'uploads/events/{self.event.id}/{name}'

    event = django.db.models.OneToOneField(
        Event,
        verbose_name=_('main image'),
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
        help_text='main image',
    )

    image = django.db.models.ImageField(
        'image',
        upload_to=saving_path,
        help_text=_('Will be rendered at 300x300 px'),
        validators=[validate_image_size],
    )

    class Meta:
        verbose_name = 'event image'
        verbose_name_plural = 'event images'
        default_related_name = 'event_image'

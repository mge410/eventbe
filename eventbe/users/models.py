import typing as tp

import django.contrib.auth.base_user
import django.contrib.auth.models
import django.core.mail
import django.db.models
import django.utils.html
from django.utils.translation import ugettext_lazy as _
import sorl.thumbnail

import users.managers


class User(
    django.contrib.auth.models.AbstractUser,
):
    class Status(django.db.models.TextChoices):
        unauthorized = 'unauth', 'unauthorized'
        authorized = 'auth', 'authorized'
        confirmed = 'conf', 'confirmed'
        admin = 'adm', 'admin'

    status = django.db.models.CharField(
        _('status'),
        default=Status.unauthorized,
        choices=Status.choices,
        help_text=_('User Status'),
        max_length=6,
    )
    coins = django.db.models.PositiveIntegerField(
        _('coins'),
        default=0,
        help_text=_('Coins'),
    )
    events_visited = django.db.models.PositiveIntegerField(
        _('events visited'),
        default=0,
        help_text=_('events visited'),
    )
    events_organized = django.db.models.PositiveIntegerField(
        _('events organized'),
        default=0,
        help_text=_('events organized'),
    )
    event_search_distance = django.db.models.PositiveIntegerField(
        _('event search distance'),
        default=100,
        help_text=_('Distance(km) to search events in'),
    )
    # desired_event_tags = django.db.models.ManyToManyField(Tag)

    objects = users.managers.UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserAvatar(django.db.models.Model):
    def saving_path(self, name):
        return f'uploads/useravatar/{self.user.id}/{name}'

    image = django.db.models.ImageField(
        'image',
        upload_to=saving_path,
        blank=True,
        help_text='Will be rendered at 300px',
    )

    class Meta:
        verbose_name = 'avatar image'
        verbose_name_plural = 'avatar images'
        default_related_name = 'avatar_image'

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

    user = django.db.models.OneToOneField(
        User,
        on_delete=django.db.models.CASCADE,
        null=True,
        unique=False,
        blank=True,
        help_text=_('user profile pic'),
        related_name='avatar',
    )

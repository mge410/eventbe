import django.contrib.auth.base_user
import django.contrib.auth.models
import django.core.mail
import django.db.models
from django.utils.translation import ugettext_lazy as _

import core.models
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
        help_text=_('Distance to search events in'),
    )
    # desired_event_tags = django.db.models.ManyToManyField(Tag)

    objects = users.managers.UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserAvatar(core.models.ImageModel):
    def saving_path(self, name) -> str:
        return f'uploads/users/{self.user.id}'

    image = django.db.models.ImageField(
        _('thumbnail'),
        upload_to=saving_path,
        help_text='Will be rendered at 300x300 px',
    )

    user = django.db.models.ForeignKey(
        User,
        on_delete=django.db.models.PROTECT,
        null=True,
        blank=True,
        help_text=_('event thumbnail'),
    )

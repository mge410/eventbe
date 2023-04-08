import django.contrib.auth.base_user
import django.contrib.auth.models
import django.core.mail
import django.db.models
from django.utils.translation import ugettext_lazy as _
import users.managers


class User(
    django.contrib.auth.models.AbstractUser,
):
    class Status(django.db.models.TextChoices):
        unauthorized = 'unauth', 'unauthorized'
        authorized = 'auth', 'authorized'
        confirmed = 'conf', 'confirmed'
        admin = 'adm', 'admin'

    # avatar
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
        help_text=_('Coins')
    )
    event_search_distance = django.db.models.PositiveIntegerField(
        _('event search distance'),
        default=100,
        help_text=_('Distance to search events in')
    )

    objects = users.managers.UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

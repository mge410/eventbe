import django.contrib.auth.models
import django.db.models

import users.models


class UserManager(django.contrib.auth.models.UserManager):
    def top_hundred_coins(self) -> django.db.models.QuerySet:
        return (
            self.get_queryset()
            .order_by(users.models.User.coins.field.name)
            .only(
                users.models.User.username,
                users.models.User.first_name,
                users.models.User.last_name,
                users.models.User.coins,
            )[:50]
        )

    def top_hundred_visited(self) -> django.db.models.QuerySet:
        return (
            self.get_queryset()
            .order_by(users.models.User.events_visited.field.name)
            .only(
                users.models.User.username,
                users.models.User.first_name,
                users.models.User.last_name,
                users.models.User.coins,
            )[:50]
        )

    def top_hundred_organized(self) -> django.db.models.QuerySet:
        return (
            self.get_queryset()
            .order_by(users.models.User.events_organized.field.name)
            .only(
                users.models.User.username,
                users.models.User.first_name,
                users.models.User.last_name,
                users.models.User.coins,
            )[:50]
        )

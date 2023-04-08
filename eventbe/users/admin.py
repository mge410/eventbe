import django.contrib.admin

import users.models


@django.contrib.admin.register(users.models.User)
class UserAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        users.models.User.username.field.name,
        users.models.User.is_active.field.name,
        users.models.User.email.field.name,
    )
    list_editable = (
        users.models.User.is_active.field.name,
        users.models.User.is_staff.field.name,
        users.models.User.is_superuser.field.name,
    )
    fields = (
        users.models.User.username.field.name,
        users.models.User.first_name.field.name,
        users.models.User.last_name.field.name,
        users.models.User.coins.field.name,
        users.models.User.events_visited.field.name,
        users.models.User.events_organized.field.name,
        users.models.User.event_search_distance.field.name,
    )

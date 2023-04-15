import django.contrib.admin

import users.models


class UserAvatar(django.contrib.admin.TabularInline):
    model = users.models.UserAvatar
    extra = 1

    readonly_fields = (model.image_tmb,)


@django.contrib.admin.register(users.models.User)
class UserAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        users.models.User.username.field.name,
        users.models.User.email.field.name,
        users.models.User.is_staff.field.name,
        users.models.User.is_superuser.field.name,
    )

    list_editable = (
        users.models.User.is_staff.field.name,
        users.models.User.is_superuser.field.name,
    )

    inlines = (UserAvatar,)

    # filter_horizontal = [
    #     users.models.User.desired_event_tags.field.name,
    # ]

    exclude = (
        users.models.User.password.field.name,
        users.models.User.last_login.field.name,
        users.models.User.groups.field.name,
        users.models.User.user_permissions.field.name,
    )

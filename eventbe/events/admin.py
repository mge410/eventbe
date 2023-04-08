import django.contrib.admin

import events.models


@django.contrib.admin.register(events.models.Event)
class EventAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        events.models.Event.title.field.name,
        events.models.Event.datetime.field.name,
        events.models.Event.status.field.name,
        events.models.Event.is_published.field.name,
        events.models.Event.is_frozen.field.name,
    )

    list_editable = (
        events.models.Event.is_published.field.name,
        events.models.Event.is_frozen.field.name,
    )

    fields = (
        events.models.Event.title.field.name,
        events.models.Event.datetime.field.name,
        events.models.Event.status.field.name,
        events.models.Event.is_published.field.name,
        events.models.Event.is_frozen.field.name,
        events.models.Event.location_x.field.name,
        events.models.Event.location_y.field.name,
        events.models.Event.organizer.field.name,
    )

    filter_horizontal = (events.models.Event.tags.field.name,)

    exclude = (events.models.Event.created_at.field.name,)


django.contrib.admin.site.register(events.models.Tag)

import django.contrib.admin

import events.models


class ThumbnailImageAdmin(django.contrib.admin.TabularInline):
    model = events.models.EventThumbnail
    extra = 1

    readonly_fields = (model.image_tmb,)


class GalleryImageAdmin(django.contrib.admin.TabularInline):
    model = events.models.EventGallery
    extra = 1

    readonly_fields = (model.image_tmb,)


class CommentAdmin(django.contrib.admin.StackedInline):
    model = events.models.EventComment
    extra = 1
    fields = (
        model.author.field.name,
        model.message.field.name,
    )
    readonly_fields = (model.author.field.name,)


@django.contrib.admin.register(events.models.Event)
class EventAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        events.models.Event.title.field.name,
        events.models.Event.date.field.name,
        events.models.Event.status.field.name,
        events.models.Event.is_published.field.name,
        events.models.Event.is_offline.field.name,
        events.models.Event.is_frozen.field.name,
    )

    list_editable = (
        events.models.Event.is_published.field.name,
        events.models.Event.is_offline.field.name,
        events.models.Event.is_frozen.field.name,
    )

    inlines = [ThumbnailImageAdmin, GalleryImageAdmin, CommentAdmin]

    fields = (
        events.models.Event.title.field.name,
        events.models.Event.date.field.name,
        events.models.Event.status.field.name,
        events.models.Event.description.field.name,
        events.models.Event.is_published.field.name,
        events.models.Event.is_frozen.field.name,
        events.models.Event.location_x.field.name,
        events.models.Event.location_y.field.name,
        events.models.Event.organizer.field.name,
        events.models.Event.tags.field.name,
    )

    # readonly_fields = (events.models.Event.description.field.name,)

    filter_horizontal = [
        events.models.Event.tags.field.name,
    ]


@django.contrib.admin.register(events.models.Tag)
class TagAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        events.models.Tag.title.field.name,
        events.models.Tag.is_active.field.name,
        events.models.Tag.slug.field.name,
    )
    list_editable = (
        events.models.Tag.is_active.field.name,
        events.models.Tag.slug.field.name,
    )
    list_display_links = (events.models.Tag.title.field.name,)

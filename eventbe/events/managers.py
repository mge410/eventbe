import django.db.models

import events.models


class EventManager(django.db.models.Manager):
    def events_list(self) -> django.db.models.QuerySet:
        return self.prefetch_events().filter(is_published=True)

    def events_detail(self) -> django.db.models.QuerySet:
        return self.prefetch_events().prefetch_related(
            django.db.models.Prefetch(
                f'{events.models.Event.comments.rel.related_name}',
                queryset=events.models.EventComment.objects.only(
                    events.models.EventComment.author.field.name,
                    events.models.EventComment.message.field.name,
                ),
            )
        )

    def prefetch_events(self) -> django.db.models.QuerySet:
        return (
            self.get_queryset()
            .select_related(
                f'{events.models.Event.event_image.related.related_name}',
            )
            .prefetch_related(
                django.db.models.Prefetch(
                    f'{events.models.Event.tags.field.name}',
                    queryset=events.models.Tag.objects.filter(
                        is_active=True
                    ).only(f'{events.models.Tag.title.field.name}'),
                )
            )
            .only(
                events.models.Event.title.field.name,
                events.models.Event.description.field.name,
                events.models.Event.date.field.name,
                events.models.Event.is_offline.field.name,
                events.models.Event.location_x.field.name,
                events.models.Event.location_y.field.name,
                f'{events.models.Event.event_image.related.related_name}'
                f'__{events.models.EventThumbnail.image.field.name}',
            )
        )

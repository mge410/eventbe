import django.forms

import events.models


class EventCreateUpdateForm(django.forms.ModelForm):
    class Meta:
        model = events.models.Event
        fields = [
            events.models.Event.title.field.name,
            events.models.Event.description.field.name,
            events.models.Event.date.field.name,
            events.models.Event.status.field.name,
            events.models.Event.location_x.field.name,
            events.models.Event.location_y.field.name,
            events.models.Event.is_offline.field.name,
            events.models.Event.tags.field.name,
        ]

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class EventCommentForm(django.forms.ModelForm):
    class Meta:
        model = events.models.EventComment
        fields = [
            events.models.EventComment.message.field.name,
        ]

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

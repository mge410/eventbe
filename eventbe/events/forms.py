import django.forms

import events.models


class EventCreateModel(django.forms.ModelForm):
    class Meta:
        model = events.models.Event
        fields = [
            events.models.Event.title.field.name,
            events.models.Event.description.field.name,
            events.models.Event.date.field.name,
            events.models.Event.status.field.name,
            events.models.Event.is_offline.field.name,
            events.models.Event.tags.field.name,
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

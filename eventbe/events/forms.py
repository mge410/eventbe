import django.forms

import events.models


class CustomDateInput(django.forms.DateInput):
    input_type = 'date'


class EventForm(django.forms.ModelForm):
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
        widgets = {
            events.models.Event.date.field.name: CustomDateInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == events.models.Event.is_offline.field.name:
                field.widget.attrs['class'] += ' form-check-input'
            if field_name == events.models.Event.location_x.field.name:
                field.widget.attrs['readonly'] = 'readonly'
            if field_name == events.models.Event.location_y.field.name:
                field.widget.attrs['readonly'] = 'readonly'


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


class EventThumbnailForm(django.forms.ModelForm):
    class Meta:
        model = events.models.EventThumbnail
        fields = [
            events.models.EventThumbnail.image.field.name,
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AddMembers(django.forms.ModelForm):
    class Meta:
        model = events.models.Event
        fields = [
            events.models.Event.members.field.name,
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AddTags(django.forms.ModelForm):
    class Meta:
        model = events.models.Tag
        fields = [
            events.models.Tag.title.field.name,
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

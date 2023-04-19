import django_filters

import events.models


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = events.models.Event
        fields = ['tags', 'status', 'is_offline']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.form.fields.values():
            field.widget.attrs['class'] = 'form-control'

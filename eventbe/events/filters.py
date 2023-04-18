import django_filters

import events.models


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = events.models.Event
        fields = ['tags', 'status', 'is_offline']

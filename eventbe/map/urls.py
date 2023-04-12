from django.urls import path

import map.views

app_name = 'map'
urlpatterns = [
    path('', map.views.MapView.as_view(), name='map'),
]

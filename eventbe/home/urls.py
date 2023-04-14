from django.urls import path

import home.views

app_name = 'homepage'
urlpatterns = [
    path('', home.views.MainView.as_view(), name='main'),
]

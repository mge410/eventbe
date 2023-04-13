from django.urls import path

import main.views

app_name = 'homepage'
urlpatterns = [
    path('', main.views.MainView.as_view(), name='main'),
]

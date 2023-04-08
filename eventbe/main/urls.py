from django.urls import path

import main.urls
import main.views

urlpatterns = [
    path('', main.views.MainView.as_view(), name='main'),
]

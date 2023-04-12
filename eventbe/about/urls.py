from django.urls import path

import about.views

app_name = 'about'
urlpatterns = [
    path('', about.views.AboutView.as_view(), name='about'),
]

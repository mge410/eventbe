import about.views
from django.urls import path

app_name = 'about'
urlpatterns = [
    path('', about.views.AboutView.as_view(), name='about'),
]

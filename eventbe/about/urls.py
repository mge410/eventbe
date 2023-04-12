from django.urls import path
import main.urls
import main.views

app_name = 'about'
urlpatterns = [
    path('', main.views.MainView.as_view(), name='about'),
]
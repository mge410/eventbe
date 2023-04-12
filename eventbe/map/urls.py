from django.urls import path
import main.urls
import main.views

app_name = 'map'
urlpatterns = [
    path('', main.views.MainView.as_view(), name='map'),
]
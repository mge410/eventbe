from django.urls import path

from download import views

app_name = 'download'
urlpatterns = [
    path(
        'data',
        views.DownloadUserDataView.as_view(),
        name='download_data',
    ),
]

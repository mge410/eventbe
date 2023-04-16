from django.urls import path

import feedback.views as views

app_name = 'feedback'
urlpatterns = [
    path(
        '',
        views.FeedbackView.as_view(),
        name='feedback',
    ),
]

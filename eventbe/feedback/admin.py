import django.contrib.admin

import feedback.models


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    list_display = (feedback.models.Feedback.id.field.name,)

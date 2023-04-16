import django.forms

import feedback.models as fmodels


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = fmodels.Feedback
        fields = [
            fmodels.Feedback.email.field.name,
            fmodels.Feedback.text.field.name,
        ]

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

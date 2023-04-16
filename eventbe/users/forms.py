from django import forms
import django.contrib.auth.forms

from users.models import User
from users.models import UserAvatar


class CustomUserCreationForm(django.contrib.auth.forms.UserCreationForm):
    email = forms.EmailField(
        label='Email', max_length=254, help_text='Enter email please'
    )

    class Meta(django.contrib.auth.forms.UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(django.contrib.auth.forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    password = None

    class Meta:
        model = User
        field_classes = {'username': django.contrib.auth.forms.UsernameField}
        fields = [
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.event_search_distance.field.name,
        ]


class UserAvatarChangeForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = [
            UserAvatar.image.field.name,
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserChangeImageForm(django.contrib.auth.forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeImageForm, self).__init__(*args, **kwargs)

    password = None

    class Meta:
        model = User
        field_classes = {'username': django.contrib.auth.forms.UsernameField}
        fields = [
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        ]

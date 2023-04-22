from django.conf import settings
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
import django.views

import users.forms
import users.models
import users.services
import users.tokens


class Register(django.views.View):
    template_name = 'users/signup.html'

    def get(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        context = {'form': users.forms.CustomUserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = users.forms.CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = settings.DEFAULT_USER_ACTIVITY
            user.save()
            avatar = users.models.UserAvatar(user=user)
            avatar.full_clean()
            avatar.save()
            if not settings.DEFAULT_USER_ACTIVITY:
                users.services.activation_email(self.request, user)

            return redirect('homepage:home')
        context = {'form': form}
        return render(request, self.template_name, context)


class ActivateUsers(django.views.generic.View):
    template_name = 'users/activate.html'

    def get(
        self, request: django.http.HttpRequest, uidb64: str, token: str
    ) -> django.http.HttpResponsePermanentRedirect:
        try:
            user = users.models.User.objects.get(
                pk=django.utils.encoding.force_str(
                    django.utils.http.urlsafe_base64_decode(uidb64)
                )
            )
        except Exception:
            user = None
        if user and users.tokens.token_7_days.check_token(user, token):
            user.is_active = True
            django.contrib.messages.success(
                request,
                'Your account has been successfully activated',
            )
            user.save()
        else:
            django.contrib.messages.error(
                request, 'The activation link is invalid.'
            )
        return render(request, self.template_name, context={})


class UsersProfile(django.views.View):
    template_name = 'users/profile.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        form = users.forms.CustomUserChangeForm(instance=user)
        avatarform = users.forms.UserAvatarChangeForm()
        context = {
            'form': form,
            'avatarform': avatarform,
            'user': user,
        }
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user

        userdataform = users.forms.CustomUserChangeForm(
            request.POST,
            request.FILES,
            instance=user,
        )

        avatarform = users.forms.UserAvatarChangeForm(
            request.POST,
            request.FILES,
            instance=user.avatar,
        )

        if userdataform.is_valid() and avatarform.is_valid():
            userdataform.save()
            avatarform.save()

        context = {
            'form': userdataform,
            'avatarform': avatarform,
            'user': user,
        }
        return render(request, self.template_name, context)

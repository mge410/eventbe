import django.conf
import django.contrib.auth.models
import django.contrib.auth.tokens
import django.contrib.sites.shortcuts
import django.core.mail
import django.http
import django.template.loader
import django.utils.encoding
import django.utils.http

import users.models
import users.tokens


def activation_email(
    request: django.http.HttpRequest,
    user: users.models.User,
) -> None:
    token = django.contrib.auth.tokens.default_token_generator.make_token(user)
    message = django.template.loader.render_to_string(
        'users/activate_user.html',
        {
            'username': user.username,
            'domain': django.contrib.sites.shortcuts.get_current_site(
                request
            ).domain,
            'uid': django.utils.http.urlsafe_base64_encode(
                django.utils.encoding.force_bytes(user.pk)
            ),
            'token': token,
            'protocol': 'https' if request.is_secure() else 'http',
            'where_to': 'users:activate',
        },
    )
    django.core.mail.send_mail(
        'Activate your account',
        message,
        django.conf.settings.MAIL_SENDER,
        [user.email],
        fail_silently=False,
    )

from django.conf import settings
from django.conf.urls.static import static
import django.contrib.admin
import django.contrib.auth.urls
import django.urls

import about.urls
import events.urls
import feedback.urls
import home.urls
import map.urls
import users.urls

urlpatterns = [
    django.urls.path('', django.urls.include(home.urls)),
    django.urls.path('about/', django.urls.include(about.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('events/', django.urls.include(events.urls)),
    django.urls.path('feedback/', django.urls.include(feedback.urls)),
    django.urls.path('map/', django.urls.include(map.urls)),
    django.urls.path('auth/', django.urls.include(users.urls)),
    django.urls.path('auth/', django.urls.include(django.contrib.auth.urls)),
]

handler404 = 'core.views.custom_page_not_found_view'
handler500 = 'core.views.custom_error_view'
handler403 = 'core.views.custom_permission_denied_view'
handler400 = 'core.views.custom_bad_request_view'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    import debug_toolbar

    urlpatterns.append(
        django.urls.path('__debug__/', django.urls.include(debug_toolbar.urls))
    )

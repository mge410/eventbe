import about.urls
from django.contrib import admin
from django.urls import include
from django.urls import path
import events.urls
import main.urls
import map.urls

urlpatterns = [
    path('', include(main.urls)),
    path('events/', include(events.urls)),
    path('about/', include(about.urls)),
    path('map/', include(map.urls)),
    path('admin/', admin.site.urls),
]

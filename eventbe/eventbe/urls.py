from django.contrib import admin
from django.urls import include
from django.urls import path

import main.urls

urlpatterns = [
    path('', include(main.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

import conf_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('conf_app.urls')),
]

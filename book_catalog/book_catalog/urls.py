from django.contrib import admin
from django.urls import include
from django.urls import path

from .yasg import urlpatterns as documentation_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('api.urls')),
]

urlpatterns += documentation_urlpatterns

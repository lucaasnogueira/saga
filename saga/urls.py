from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', include('main.urls')),
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
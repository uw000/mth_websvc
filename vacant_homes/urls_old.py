# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vacant_homes.urls')),  # vacant_homes 앱의 URL을 포함
]
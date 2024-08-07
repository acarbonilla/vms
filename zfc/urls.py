from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('vHome/', include('visitor.urls')),
    path('zfcemployee/', include('zfcemployee.urls')),
    path('manager/', include('manager.urls')),
]

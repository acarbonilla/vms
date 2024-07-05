from django.urls import path
from visitor.views import vHome, monitoringViews, permitted, denied, expired

urlpatterns = [
    path('', vHome, name='vHome'),
    path('monitoringViews/', monitoringViews, name='monitoringViews'),
    path('permitted/', permitted, name='permitted'),
    path('denied/', denied, name='denied'),
    path('expired/', expired, name='expired'),
]
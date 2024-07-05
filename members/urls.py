from django.urls import path
from .views import vmsLogin, vmsLogout, vmsRegister

urlpatterns = [
    path('', vmsLogin, name='vmsLogin'),
    path('vmsLogout/', vmsLogout, name='vmsLogout'),
    path('vmsRegister/', vmsRegister, name='vmsRegister'),

    ]

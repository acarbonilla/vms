from django.urls import path
from manager.views import managerPage, mDeptForm, mDeptFormEdit, mDeptList

urlpatterns = [
    path('managerPage/', managerPage, name='managerPage'),
    path('mDeptList/',  mDeptList, name='mDeptList'),
    path('mDeptForm/', mDeptForm, name='mDeptForm'),
    path('mDeptFormEdit/<str:pk>/', mDeptFormEdit, name='mDeptFormEdit'),
]
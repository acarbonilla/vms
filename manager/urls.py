from django.urls import path
from manager.views import (managerPage, mDeptForm, mDeptFormEdit, mDeptList, mUserList,
                          pdfListView, pdfDetails)


urlpatterns = [
    path('managerPage/', managerPage, name='managerPage'),
    path('mDeptList/',  mDeptList, name='mDeptList'),
    path('mUserList/', mUserList, name='mUserList'),

    # PDF

    path('pdfListView/', pdfListView, name='pdfListView'),
    path('pdfDetails/<str:pk>/', pdfDetails, name='pdfDetails'),

    path('mDeptForm/', mDeptForm, name='mDeptForm'),
    path('mDeptFormEdit/<str:pk>/', mDeptFormEdit, name='mDeptFormEdit'),
]
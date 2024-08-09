from django.urls import path
from manager.views import (managerPage, mDeptForm, mDeptFormEdit, mDeptList, mUserList,
                           pdfListView, pdfDetails, approved_csv)

urlpatterns = [
    path('managerPage/', managerPage, name='managerPage'),
    path('mDeptList/', mDeptList, name='mDeptList'),
    path('mUserList/', mUserList, name='mUserList'),

    # PDF

    path('pdfListView/', pdfListView, name='pdfListView'),
    path('pdfDetails/<str:pk>/', pdfDetails, name='pdfDetails'),

    # CSV
    path('approved_csv/', approved_csv, name='approved_csv'),

    path('mDeptForm/', mDeptForm, name='mDeptForm'),
    path('mDeptFormEdit/<str:pk>/', mDeptFormEdit, name='mDeptFormEdit'),

]

from django.urls import path
from manager.views import (managerPage, mDeptForm, mDeptFormEdit, mDeptList, mUserList,
                           render_pdf_view, pdfListView, pdfDetails)


urlpatterns = [
    path('managerPage/', managerPage, name='managerPage'),
    path('mDeptList/',  mDeptList, name='mDeptList'),
    path('mUserList/', mUserList, name='mUserList'),

    # PDF
    path('render_pdf_view/', render_pdf_view, name='render_pdf_view'),
    path('pdfListView/', pdfListView, name='pdfListView'),
    path('pdfDetails/<str:pk>/', pdfDetails, name='pdfDetails'),

    path('mDeptForm/', mDeptForm, name='mDeptForm'),
    path('mDeptFormEdit/<str:pk>/', mDeptFormEdit, name='mDeptFormEdit'),
]
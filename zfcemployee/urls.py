from django.urls import path
from zfcemployee.views import (zfcEmployees, VisitorRequestFormEditView, zfcPermitted, zfcExpired, zfcDenied,
                               zfcPermittedDetails, zfcProfile, zfcStaffEmployees)

urlpatterns = [
    path('', zfcEmployees, name='zfcEmployees'),
    path('zfcPermitted/', zfcPermitted, name='zfcPermitted'),
    path('zfcExpired/', zfcExpired, name='zfcExpired'),
    path('zfcDenied/', zfcDenied, name='zfcDenied'),
    path('zfcStaffEmployees/', zfcStaffEmployees, name='zfcStaffEmployees'),

    # Edit Form
    path('VisitorRequestFormEditView/<str:pk>/', VisitorRequestFormEditView, name='VisitorRequestFormEditView'),
    path('zfcProfile/', zfcProfile, name='zfcProfile'),
    # Details
    path('zfcPermittedDetails/<str:pk>/', zfcPermittedDetails, name='zfcPermittedDetails'),

]
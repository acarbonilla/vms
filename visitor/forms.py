from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from core.models import EmpName
from visitor.models import RequestForm


class VisitorRequestForm(ModelForm):
    class Meta:
        model = RequestForm
        fields = ('fullName', 'companyName', 'companyAddress', 'reasonOfRequest', 'dateFrom', 'dateTo', 'contactPerson',
                  'appointment', 'noAppointment', 'guard', 'placesVisited', 'bdv', 'soreThroat', 'cold', 'mumps',
                  'skin', 'styes', 'jaundice', 'cuts', 'infection', 'typhoid', 'country', 'temp', 'agreement',
                  'dateSigned')


class VisitorRequestFormEdit(ModelForm):
    class Meta:
        model = RequestForm
        fields = ('approved', 'comment')




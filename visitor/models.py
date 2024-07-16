from django.contrib.auth.models import User
from django.db import models
import random
from django.utils import timezone

from core.models import EmpName


# This is for random Ticket method
def requestID():
    return str("ZFC") + str(random.randint(1000000, 9999999))


class RequestForm(models.Model):
    id = models.CharField(max_length=10, default=requestID, primary_key=True, editable=False)
    fullName = models.CharField(max_length=100, verbose_name='Fullname')
    companyName = models.CharField(max_length=50, verbose_name='Company Name')
    companyAddress = models.CharField(max_length=100, verbose_name='Company Address')
    reasonOfRequest = models.TextField(null=True, blank=True, verbose_name='Reason For Request')

    dateFrom = models.DateField(auto_now=False, verbose_name='Start Date')
    dateTo = models.DateField(auto_now=False, verbose_name='End Date')
    contactPerson = models.ForeignKey(EmpName, on_delete=models.CASCADE, verbose_name='ZFC Employee')

    appointment = models.BooleanField(editable=True)
    noAppointment = models.BooleanField(editable=True)
    guard = models.CharField(max_length=200, verbose_name='SG in Charge')

    # Health Check
    placesVisited = models.CharField(max_length=200, verbose_name='Last Places Visited')
    bdv = models.BooleanField(editable=True)
    soreThroat = models.BooleanField(editable=True)
    cold = models.BooleanField(editable=True)
    mumps = models.BooleanField(editable=True)
    skin = models.BooleanField(editable=True)
    styes = models.BooleanField(editable=True)
    jaundice = models.BooleanField(editable=True)
    cuts = models.BooleanField(editable=True)
    infection = models.BooleanField(editable=True)
    typhoid = models.BooleanField(editable=True)
    country = models.CharField(max_length=100, verbose_name="Last Countries Visited")
    temp = models.IntegerField()

    agreement = models.BooleanField(editable=True, default=True)
    dateSigned = models.DateField(auto_now=False, verbose_name='Date Signed')

    # Approval
    approved = models.CharField(
        max_length=10,
        choices=[("Review", "Review"), ("Permitted", "Permitted"), ("Denied", "Denied")],
        default='Review',
        verbose_name='For approval'

    )
    comment = models.TextField(null=True, blank=True, verbose_name='comment here')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.id} - {self.approved}: {self.comment}'

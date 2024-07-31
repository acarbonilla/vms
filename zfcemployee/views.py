
from datetime import timedelta, datetime
import time
from django.contrib import messages


from django.db.models.functions import Now
from django.shortcuts import render, redirect

from visitor.forms import VisitorRequestFormEdit
from visitor.models import RequestForm
from zfcemployee.forms import ProfileForm

# This is for login required
from django.contrib.auth.decorators import login_required


@login_required(login_url='vmsLogin')
def zfcEmployees(request):
    visitorReq = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Review")
    visitorReqCount = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Review").count()
    context = {'visitorReq': visitorReq, 'visitorReqCount': visitorReqCount, 'title': 'Request Review'}
    return render(request, 'staff/zfcemp.html', context)


@login_required(login_url='vmsLogin')
def zfcPermitted(request):
    zfcVisitorPermitted = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Approve")
                           .filter(dateTo__gte=Now() - timedelta(1)))
    zfcVisitorPermittedCount = (
        RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Approve")
        .filter(dateTo__gte=Now() - timedelta(1))).count()
    context = {'zfcVisitorPermitted': zfcVisitorPermitted, 'zfcVisitorPermittedCount': zfcVisitorPermittedCount,
               'title': 'Request Approved'}
    return render(request, 'staff/zfcPermitted.html', context)


@login_required(login_url='vmsLogin')
def zfcExpired(request):
    one_week_ago = datetime.today() - timedelta(days=7)
    zfcVisitorExpired = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Approve")
                         .filter(dateTo__lt=Now() - timedelta(1))).filter(dateTo__gte=one_week_ago)
    zfcVisitorExpiredCount = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Approve")
                              .filter(dateTo__lt=Now() - timedelta(1))).filter(dateTo__gte=one_week_ago).count()
    context = {'zfcVisitorExpired': zfcVisitorExpired, 'zfcVisitorExpiredCount': zfcVisitorExpiredCount,
               'title': 'Request Expired'}
    return render(request, 'staff/zfcPermitExpired.html', context)


@login_required(login_url='vmsLogin')
def zfcDenied(request):
    one_week_ago = datetime.today() - timedelta(days=7)
    zfcVisitorDenied = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Denied",
                                                  created__gte=one_week_ago)
    zfcVisitorDeniedCount = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Denied",
                                                       created__gte=one_week_ago).count()
    context = {'zfcVisitorDenied': zfcVisitorDenied, 'zfcVisitorDeniedCount': zfcVisitorDeniedCount,
               'title': 'Request Denied'}
    return render(request, 'staff/zfcRequestDenied.html', context)


# This is for the details and for all details in staff app

def zfcPermittedDetails(request, pk):
    zfcPD = RequestForm.objects.get(id=pk)
    context = {'zfcPD': zfcPD, 'title': zfcPD.id}
    return render(request, 'staff/zfcPDdetails.html', context)


# This is for Edit Form/View that the form is located in visitor app .form
@login_required(login_url='vmsLogin')
def VisitorRequestFormEditView(request, pk):
    proved = RequestForm.objects.get(id=pk)
    form = VisitorRequestFormEdit(request.POST or None, instance=proved)
    if form.is_valid():
        form.save()
        return redirect('zfcEmployees')
    context = {'form': form, 'title': 'Approval'}
    return render(request, 'staff/requestEditForm.html', context)


@login_required(login_url='vmsLogin')
def zfcProfile(request):
    if request.method == "POST":
        form = ProfileForm(request.user, request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('zfcEmployees')
        else:
            messages.error(request, "Company ID Taken or You already filled up this form.")
    else:
        form = ProfileForm(request.user)

    context = {'form': form, 'title': 'ZFC Employee Profile'}
    return render(request, 'staff/zfcprofile.html', context)



from datetime import timedelta

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
    context = {'visitorReq': visitorReq, 'visitorReqCount': visitorReqCount}
    return render(request, 'staff/zfcemp.html', context)


@login_required(login_url='vmsLogin')
def zfcPermitted(request):
    zfcVisitorPermitted = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Permitted")
                           .filter(dateTo__gte=Now() - timedelta(1)))
    zfcVisitorPermittedCount = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Permitted")
                           .filter(dateTo__gte=Now() - timedelta(1))).count()
    context = {'zfcVisitorPermitted': zfcVisitorPermitted, 'zfcVisitorPermittedCount': zfcVisitorPermittedCount}
    return render(request, 'staff/zfcPermitted.html', context)


@login_required(login_url='vmsLogin')
def zfcExpired(request):
    zfcVisitorExpired = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Permitted")
                         .filter(dateTo__lt=Now() - timedelta(1)))
    zfcVisitorExpiredCount = (RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Permitted")
                         .filter(dateTo__lt=Now() - timedelta(1))).count()
    context = {'zfcVisitorExpired': zfcVisitorExpired, 'zfcVisitorExpiredCount': zfcVisitorExpiredCount}
    return render(request, 'staff/zfcPermitExpired.html', context)


@login_required(login_url='vmsLogin')
def zfcDenied(request):
    zfcVisitorDenied = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Denied")
    zfcVisitorDeniedCount = RequestForm.objects.filter(contactPerson__member_id=request.user.id, approved="Denied").count()
    context = {'zfcVisitorDenied': zfcVisitorDenied, 'zfcVisitorDeniedCount': zfcVisitorDeniedCount}
    return render(request, 'staff/zfcRequestDenied.html', context)


# This is for the details and for all details in staff app

def zfcPermittedDetails(request, pk):
    zfcPD = RequestForm.objects.get(id=pk)
    context = {'zfcPD': zfcPD}
    return render(request, 'staff/zfcPDdetails.html', context)


# This is for Edit Form/View that the form is located in visitor app .form
@login_required(login_url='vmsLogin')
def VisitorRequestFormEditView(request, pk):
    proved = RequestForm.objects.get(id=pk)
    form = VisitorRequestFormEdit(request.POST or None, instance=proved)
    if form.is_valid():
        form.save()
        return redirect('zfcEmployees')
    context = {'form': form}
    return render(request, 'staff/requestEditForm.html', context)


@login_required(login_url='vmsLogin')
def zfcProfile(request):
    form = ProfileForm(request.user, request.POST)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('zfcEmployees')
    else:
        form = ProfileForm(request.user)

    context = {'form': form}
    return render(request, 'staff/zfcprofile.html', context)


# This is for the Staff employees
@login_required(login_url='vmsLogin')
def zfcStaffEmployees(request):
    staff = RequestForm.objects.all()
    context = {'staff': staff}
    return render(request, 'staff/zfcStaffEmp.html', context)

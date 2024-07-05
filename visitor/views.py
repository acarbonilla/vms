from django.shortcuts import render
from django.db.models.functions import Now
from visitor.forms import VisitorRequestForm
from django.shortcuts import render, redirect

from visitor.models import RequestForm


# This is for expired Request Pass
from datetime import timedelta


def vHome(request):
    submitted = False
    if request.method == "POST":
        form = VisitorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoringViews')
    else:
        form = VisitorRequestForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form': form}
    return render(request, 'visitor/vHomeView.html', context)


def monitoringViews(request):
    visitorReview = RequestForm.objects.filter(approved="Review")
    visitorReviewCount = RequestForm.objects.filter(approved="Review").count()
    context = {'visitorReview': visitorReview, 'visitorReviewCount': visitorReviewCount}
    return render(request, 'visitor/monitoringViews.html', context)


def permitted(request):
    visitorPermitted = RequestForm.objects.filter(approved="Permitted").filter(dateTo__gte=Now() - timedelta(1))
    visitorPermittedCount = RequestForm.objects.filter(approved="Permitted").filter(dateTo__gte=Now() - timedelta(1)).count()
    context = {'visitorPermitted': visitorPermitted, 'visitorPermittedCount': visitorPermittedCount}
    return render(request, 'visitor/permitted.html', context)


def denied(request):
    visitorDenied = RequestForm.objects.filter(approved="Denied")
    visitorDeniedCount = RequestForm.objects.filter(approved="Denied").count()
    context = {'visitorDenied': visitorDenied, 'visitorDeniedCount': visitorDeniedCount}
    return render(request, 'visitor/requestDenied.html', context)


def expired(request):
    visitorExpired = RequestForm.objects.filter(approved="Permitted").filter(dateTo__lt=Now() - timedelta(1))
    visitorExpiredCount = RequestForm.objects.filter(approved="Permitted").filter(dateTo__lt=Now() - timedelta(1)).count()
    context = {'visitorExpired': visitorExpired, 'visitorExpiredCount': visitorExpiredCount}
    return render(request, 'visitor/permitExpired.html', context)


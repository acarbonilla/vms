from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
# This is for login required
from django.contrib.auth.decorators import login_required

from core.models import Department
from manager.forms import DeptForm, DeptFormEdit
from visitor.models import RequestForm

# This is for pdf download
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# This is for expired Request Pass
from datetime import timedelta, datetime

# This is for counting per user assigned
from django.db.models import Count


# This is for the Staff employees
@login_required(login_url='vmsLogin')
def managerPage(request):
    requestCountPermitted = RequestForm.objects.filter(approved="Permitted").count()
    requestCountDenied = RequestForm.objects.filter(approved="Denied").count()
    requestCountPending = RequestForm.objects.filter(approved="Review").count()
    # counting all request within 30 days
    requestCount = requestCountPermitted + requestCountDenied + requestCountPending

    # This is for who are active, login, and others under the User auth
    one_day = datetime.today() - timedelta(minutes=30)
    userLogging = User.objects.filter(last_login__gte=one_day, is_superuser=False)

    # This is for overall Permitted per user
    employee = RequestForm.objects.values(
        'contactPerson__member__first_name', 'contactPerson__member__last_name'
    ).annotate(
        requestID=Count('id'),
    ).filter(approved="Permitted")

    # This is for overall Denied per user
    employeeDenied = RequestForm.objects.values(
        'contactPerson__member__first_name', 'contactPerson__member__last_name'
    ).annotate(
        requestID=Count('id'),
    ).filter(approved="Denied")

    # This is for overall Pending/Review per user
    employeeReview = RequestForm.objects.values(
        'contactPerson__member__first_name', 'contactPerson__member__last_name'
    ).annotate(
        requestID=Count('id'),
    ).filter(approved="Review")

    # This is for all active user
    userList = User.objects.filter(is_superuser=False)

    # This is for the Visitors Company
    vCompany = RequestForm.objects.values('companyName').annotate(Count('companyName')).order_by('companyName')

    context = {'title': 'Manager', 'requestCount': requestCount, 'requestCountPermitted': requestCountPermitted,
               'requestCountDenied': requestCountDenied, 'requestCountPending': requestCountPending,
               'userLogging': userLogging, 'employee': employee, 'employeeDenied': employeeDenied,
               'employeeReview': employeeReview, 'userList': userList, 'vCompany': vCompany}
    return render(request, 'manager/managerPage.html', context)


# This is the Department List
@login_required(login_url='vmsLogin')
def mDeptList(request):
    dept = Department.objects.all()
    deptCount = Department.objects.all().count()
    context = {'dept': dept, 'title': 'Department List', 'deptCount': deptCount}
    return render(request, 'manager/deptList.html', context)


# This is for the Department Form

def mDeptForm(request):
    submitted = False
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mDeptList')
    else:
        form = DeptForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form': form, 'title': 'Department_Form'}
    return render(request, 'manager/departmentForm.html', context)


# Department Edit Form
@login_required(login_url='vmsLogin')
def mDeptFormEdit(request, pk):
    dept = Department.objects.get(id=pk)
    form = DeptFormEdit(request.POST or None, instance=dept)
    if form.is_valid():
        form.save()
        return redirect('mDeptList')
    context = {'form': form, 'title': 'Edit Department'}
    return render(request, 'manager/deptEditForm.html', context)


# This is the list for user

def mUserList(request):
    userList = User.objects.filter(is_superuser=False)
    userListCount = User.objects.filter(is_superuser=False).count()
    context = {'userList': userList, 'title': 'Listed User', 'userListCount': userListCount}
    return render(request, 'manager/listedUser.html', context)


# This is for PDF Download
@login_required(login_url='vmsLogin')
def pdfListView(request):
    pdfList = RequestForm.objects.filter(approved="Permitted")
    pdfListCount = RequestForm.objects.filter(approved="Permitted").count()
    context = {'pdfList': pdfList, 'pdfListCount': pdfListCount}
    return render(request, 'pdf/pdf_main.html', context)


@login_required(login_url='vmsLogin')
def pdfDetails(request, pk):
    pdf_details = RequestForm.objects.get(id=pk)
    template_path = 'pdf/pdf1.html'
    context = {'pdf_details': pdf_details, 'title': pdf_details.id}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # if want to download right away without viewing
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # View and download
    response['Content-Disposition'] = 'filename="file.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


@login_required(login_url='vmsLogin')
def render_pdf_view(request):
    template_path = 'pdf/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # if want to download right away without viewing
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # View and download
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

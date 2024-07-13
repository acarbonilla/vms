from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
# This is for login required
from django.contrib.auth.decorators import login_required

from core.models import Department
from manager.forms import DeptForm, DeptFormEdit
from visitor.models import RequestForm


# This is for the Staff employees
@login_required(login_url='vmsLogin')
def managerPage(request):
    staff = RequestForm.objects.all()
    context = {'staff': staff, 'title': 'Manager'}
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
    userList = User.objects.all()
    userListCount = User.objects.all().count()
    context = {'userList': userList, 'title': 'Listed User', 'userListCount': userListCount}
    return render(request, 'manager/listedUser.html', context)

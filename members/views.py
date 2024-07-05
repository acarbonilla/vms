from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from members.forms import UserForm


# This is for Login and logout


def vmsLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('zfcStaffEmployees')
            else:
                return redirect('zfcEmployees')

        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Username and Password didn't match. Try Again")
            return redirect('vmsLogin')

    else:
        return render(request, 'members/login.html', {})


def vmsLogout(request):
    logout(request)
    # messages.success(request, "Successfully Logout.")
    return redirect('vmsLogin')


def vmsRegister(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('zfcProfile')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'members/vmsregister.html', context)

from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from log.models import Log


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


def logout(request):
    print("hi")
    auth_logout(request)
    return redirect('/')


@login_required
def user_logs(request, user):
    logs = Log.objects.filter(created_by=user)
    for log in logs:
        print("HH: ", log.log)
    print("logs: ", logs.all())
    data = {
        'user': user,
        'logs': logs
    }
    return render(request, 'user_logs.html', data)
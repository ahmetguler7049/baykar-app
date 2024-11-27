from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('team_dashboard')
        else:
            messages.error(request, "Geçersiz email veya şifre.")
            return redirect('login')

    return render(request, 'authentication/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

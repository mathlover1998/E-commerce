from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, logout



def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=email):
                messages.error(
                    request, 'This email is taken! Please log in instead!')
                return redirect('handleLogin')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request, 'Confirm password must be the same with password!')
                return redirect('signUp')
            user = User.objects.create_user(
                username=email, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('index')

    return render(request, 'authentication/login-signup.html',{"form":form,"is_login":False})


def handle_login(request):
    return render(request, 'authentication/login-signup.html')


def handle_logout(request):
    return redirect('/auth/login')

from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login, logout,authenticate
from .utils import send_email
from .models import User




def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')

            if User.objects.filter(username=username):
                messages.error(
                    request, 'This username is taken! Please log in instead!')
                return redirect('handleLogin')
            elif User.objects.filter(email=email):
                messages.error(
                    request, 'This email is taken! Please log in instead!')
                return redirect('handleLogin')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request, 'Confirm password must be the same with password!')
                return redirect('signUp')
            # send_email(email)
            user = User.objects.create_user(
                username=email, email=email, password=password)
            
            user.save()
            login(request, user)
            return redirect('index')

    return render(request, 'authentication/login-signup.html',{"form":form,"is_login":False})


def handle_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                if not User.objects.filter(username = username).exists():
                    messages.error(request,"This account does not exist! Please Sign up first!")
                    return redirect('signUp')
                else:
                    messages.error(request,"Invalid password!")



    return render(request, 'authentication/login-signup.html',{"form":form,"is_login":True})


def handle_logout(request):
    logout(request)
    return redirect('handleLogin')



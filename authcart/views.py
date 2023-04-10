from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method =='POST':
        email = request.POST['email']
        if User.objects.filter(username = email):
            messages.error(request, 'This email is taken!')
            return redirect('/auth/signup')
        else:
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password != confirm_password:
                messages.error(request,'This password confirmation does not match!')
                return redirect('/auth/signup')
            else:
                user = User.objects.create_user(username=email,email=email,password=password)
                user.save()
                return redirect('index')
                


    else:
        return render(request,'authentication/signup.html')

def handle_login(request):
    return render(request,'authentication/login.html')

def handle_logout(request):
    return redirect('/auth/login')
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def orders(request):
    return render(request,'orders.html')

def profile(request):
    return render(request,'profile.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

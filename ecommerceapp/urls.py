from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('blog',views.blog, name='blog'),
    path('orders',views.orders, name='orders'),
    path('profile',views.profile, name='profile'),
    path('cart',views.cart, name='cart'),
    
]
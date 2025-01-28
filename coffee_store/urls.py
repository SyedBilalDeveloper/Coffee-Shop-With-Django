from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'), 
]



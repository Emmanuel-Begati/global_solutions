from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('team/', views.team, name='team'),
    path('base/', views.base, name='base'),
    path('faqs/', views.faqs, name='faqs'),
]
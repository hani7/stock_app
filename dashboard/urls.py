from django.urls import path
from django.contrib import admin
from  . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('profile/', views.profile, name='profile')


    ]


      
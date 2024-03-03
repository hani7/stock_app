
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register', user_view.register , name = 'user-register'),
    path('login', auth_views.LoginView.as_view() , name = 'user-login'),
    path('logout', auth_views.LogoutView.as_view() , name = 'user-logout'),


    
]

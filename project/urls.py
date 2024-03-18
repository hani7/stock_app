
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from dashboard import views


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('dashboard.urls')),
    path('register', user_view.register , name = 'user-register'),
    path('profile', auth_views.LoginView.as_view(template_name='user/profile.html') , name = 'user-profile'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html') , name = 'user-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='user/logout.html') , name = 'user-logout'),


    
]

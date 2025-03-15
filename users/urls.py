from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, dashboard

urlpatterns = [
    path('register/', register, name='register'),  # User registration page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # User login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # User logout functionality
    path('dashboard/', dashboard, name='dashboard'),  # User dashboard (clients & lawyers)
]
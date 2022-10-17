from django.urls import path
from .views import Registration, admin_view, delete_view, edit_view, home, login_view, logout_view, superuser_view, user_view, vehicle_view

urlpatterns = [
    path('register',Registration,name='register'),
    path('login_view',login_view,name='login_view'),
    path('home',home,name='home'),
    path('logout',logout_view,name='logout'),
    path('user',user_view,name='user'),
    path('admin_view',admin_view,name='admin_view'),
    path('superuser',superuser_view,name='superuser'),
    path('edit/<int:pk>',edit_view,name='edit'),
    path('delete/<int:pk>',delete_view,name='delete'),
]

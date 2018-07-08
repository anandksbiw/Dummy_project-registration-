from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'form_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('save/', views.save, name='save'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('librarian/', views.librarian, name='librarian'),
    path('uploaded/', views.uploaded, name='uploaded'),
    path('change_password/',views.change_password,name='password_change'),


]

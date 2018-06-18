from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('save/', views.save, name='save'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile')
]

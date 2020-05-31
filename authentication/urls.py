from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
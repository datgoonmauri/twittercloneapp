from django.urls import path
from notifications import views


urlpatterns = [
   path('notification/', views.notification),
]
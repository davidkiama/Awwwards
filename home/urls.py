from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/<pk>/', views.profile, name='profile'),
]

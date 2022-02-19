from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name='login' ),
    path('register/', views.registerPage, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
]
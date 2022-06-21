from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/', views.logoutUser, name='logout'),
]

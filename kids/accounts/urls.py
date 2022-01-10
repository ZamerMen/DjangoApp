from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view, name='login'),
    path('register/', RegisterUser.as_view(), name='register')
]
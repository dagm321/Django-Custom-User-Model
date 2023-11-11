from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginpage, name='loginpage'),
    path('home/', views.home, name='home'),
]
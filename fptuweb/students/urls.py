from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='students_home'),
    path("login/", views.login, name='students_login'),
]
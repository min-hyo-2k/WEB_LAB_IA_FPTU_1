from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="teachers_register"),
    path("", views.home, name="teachers_home"),
]
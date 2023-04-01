from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="teachers_register"),
    path("", views.home, name="teachers_home"),
    path("class-list/", views.teacher_class, name="teachers_class"),
    path("student-list/", views.student_list, name="teachers_student_list"),
]
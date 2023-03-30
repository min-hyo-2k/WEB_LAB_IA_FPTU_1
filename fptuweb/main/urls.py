from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='main_home'),
    path("test/<int:id>", views.test, name='main_test')
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("test/<int:id>", views.test, name='test')
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='main_home'),
    path("test/<int:id>", views.test, name='main_test'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

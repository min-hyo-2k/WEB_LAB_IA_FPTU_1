from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='students_home'),
    path("show-all-demo/", views.show_all_demo, name='students_show_all_demo'),
    path("show-course-demo/", views.show_course_demo, name="students_show_course_demo"),
    path('chat/', views.chat, name='chat'),
    path('chat/delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('chat/edit/<int:message_id>/', views.edit_message, name='edit_message'),
]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def test(response, id):
    student = Student.objects.get(id=id)
    student_course = StudentCourse.objects.filter(student=id)
    course_list = [item.course for item in student_course]
    print(course_list)
    return render(response, "main/test.html", {'student' : student, 'course_list' : course_list})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('students_home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'main/home.html')


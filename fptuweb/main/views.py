from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserLoginForm
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'students/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'main/home.html')


from django.shortcuts import render
from django.http import HttpResponse
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
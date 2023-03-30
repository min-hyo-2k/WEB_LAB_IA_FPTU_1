from django.shortcuts import render
from main.models import *

# Create your views here.
def home(response):
    return render(response, "students/home.html", {})

def login(resonse):
    test = Student.objects.all()
    print(Student)
    return render(resonse, "students/login.html", {})
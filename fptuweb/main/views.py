from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def test1(response, id):
    student = Student.objects.get(id=id)
    sc = StudentCourse.objects.get(id=id)
    #sca = StudentCourse.objects.all() #must do in html queryset, httpsresponse will not show queryset
    print(sc.student.curriculum) 
    return HttpResponse(f"<h1>{student.roll_number}</h1>")
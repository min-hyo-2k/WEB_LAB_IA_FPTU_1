from django.shortcuts import render
from main import models as main_model

# Create your views here.
def home(response):
    return render(response, "students/home.html", {})

def show_all_demo(request):
    id = request.GET.get('id', 1)
    student_id = main_model.Student.objects.get(id=id)
    student_course = main_model.StudentCourse.objects.filter(student=id)
    for item in student_course:
        avg_mark = calculate_weighted_total(student_id=id, course_id=item.course.id)
        item.avg_mark = avg_mark
        item.save()
    return render(request, "students/show_all_demo.html", {'student' : student_id, 'student_course' : student_course})

def show_course_demo(request):
    id = request.GET.get('id', 1)
    student_id = main_model.Student.objects.get(id=id)
    course = main_model.Course.objects.all()
    return render(request, "students/show_course_demo.html", {'student' : student_id, 'course' : course})

def calculate_weighted_total(student_id, course_id):
    # Retrieve the CoursePartMark instances related to the specific course
    course_part_marks = main_model.CoursePartMark.objects.filter(course_id=course_id)

    # Retrieve the CourseMark instances related to the specific student and course
    course_marks = main_model.CourseMark.objects.filter(student_id=student_id, course_id=course_id)

    # Calculate the total weighted score
    total_weighted_score = 0
    for course_mark in course_marks:
        part_mark = course_mark.mark
        weight = course_part_marks.get(id=course_mark.part_mark_id).weight
        total_weighted_score += part_mark * weight / 100

    return total_weighted_score
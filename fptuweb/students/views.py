from django.shortcuts import render
from main import models as main_model

# Create your views here.
def home(request):
    roll_number = request.user.username
    student = main_model.Student.objects.get(roll_number=roll_number)
    return render(request, "students/home.html", {'student' : student})

def show_all_demo(request):
    roll_number = request.user.username
    student = main_model.Student.objects.get(roll_number=roll_number)
    student_course = main_model.StudentCourse.objects.filter(student__roll_number=roll_number)
    for item in student_course:
        avg_mark = calculate_weighted_total(student_code=roll_number, course_code=item.course.course_code)
        item.avg_mark = avg_mark
        item.save()
    return render(request, "students/show_all_demo.html", {'student' : student, 'student_course' : student_course})


def show_course_demo(request):
    roll_number = request.user.username
    student = main_model.Student.objects.get(roll_number=roll_number)
    course = main_model.Course.objects.all()
    return render(request, "students/show_course_demo.html", {'student' : student, 'course' : course})

def calculate_weighted_total(student_code, course_code):
    # Retrieve the CoursePartMark instances related to the specific course
    course_part_marks = main_model.CoursePartMark.objects.filter(course__course_code=course_code)

    # Retrieve the CourseMark instances related to the specific student and course
    course_marks = main_model.CourseMark.objects.filter(student__roll_number=student_code, course__course_code=course_code)

    # Calculate the total weighted score
    total_weighted_score = 0
    for course_mark in course_marks:
        part_mark = course_mark.mark
        weight = course_part_marks.get(id=course_mark.part_mark_id).weight
        total_weighted_score += part_mark * weight / 100

    return total_weighted_score

# CRUD
from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import MessageForm

def chat(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')

    context = {'messages': messages, 'form': form}
    return render(request, 'students/chat.html', context)

def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('chat')

def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    form = MessageForm(instance=message)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('chat')

    context = {'form': form}
    return render(request, 'students/edit_message.html', context)

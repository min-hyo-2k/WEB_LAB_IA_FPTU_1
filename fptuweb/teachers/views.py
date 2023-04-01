from django.shortcuts import render, redirect
from .forms import RegistrationForm
from main import models as m
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegistrationForm()
    return render(request, "teachers/register.html", {"form": form})

# Create your views here.
@login_required(login_url="/login")
def home(request):
    u = request.user.username
    print(u)
    teacher = m.Teacher.objects.get(teacher_code__iexact=u)
    print(teacher)
    
    return render(request, "teachers/home.html", {"teacher" : teacher})

@login_required(login_url="/login")
def teacher_class(request):
    u = request.user.username
    print(u)
    teacher = m.Teacher.objects.get(teacher_code__iexact=u)
    print(teacher)
    teacher_class = m.GroupCourseTeacher.objects.filter(teacher__teacher_code=teacher.teacher_code)
    print(teacher_class)
    return render(request, "teachers/teacher_class.html", {"teacher_class" : teacher_class})

@login_required(login_url="/login")
def student_list(request):
    group = request.GET.get('group')
    course = request.GET.get('course')
    group_course= m.GroupCourse.objects.get(group__name=group, course__course_code=course)
    student_group_course = m.GroupCourseStudent.objects.filter(group_course=group_course.id)
    s_list = []
    for item in student_group_course:
        studentx = m.StudentCourse.objects.filter(course__course_code=course, group__name=group)
        # studentx = m.StudentCourse.objects.filter(student=item.students.id, course__course_code=course, group__name=group, status='S').first()
        for s in studentx:
            student = str(s.student.roll_number) +" - "+ str(s.student.name)
            s_list.append(student)
    print(s_list)
    return render(request, "teachers/student_list.html", {"group" : group, "course" : course, "s_list" : s_list})

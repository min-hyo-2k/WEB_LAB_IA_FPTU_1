from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=30, unique=True)
    major = models.CharField(max_length=10)
    specialization = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=10, unique=True)
    credit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} : {self.course_code}"


class CurriculumCourse(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('curriculum', 'course')

    def __str__(self):
        return f"{self.curriculum.name} : {self.course.name}"


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-binary'),
    )

    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    date_of_join = models.DateField()
    card_id = models.CharField(max_length=12, unique=True)
    date_of_issue = models.DateField()
    curriculum = models.ForeignKey(Curriculum, on_delete=models.SET_NULL, null=True)
    current_term = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} : {self.roll_number}"


class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-binary'),
    )

    teacher_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    date_of_join = models.DateField()
    card_id = models.CharField(max_length=12, unique=True)
    date_of_issue = models.DateField()

    def __str__(self):
        return f"{self.name} : {self.teacher_code}"


class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class GroupCourse(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'course')

    def __str__(self):
        return f"{self.group.name} : {self.course.name}"


class GroupCourseStudent(models.Model):
    group_course = models.ForeignKey(GroupCourse, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('group_course', 'students')

    def __str__(self):
        return f"{self.students.name} : {self.group_course.__str__()}"


class GroupCourseTeacher(models.Model):
    group_course = models.ForeignKey(GroupCourse, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('group_course', 'teacher')

    def __str__(self):
        return f"{self.group_course.__str__()} : {self.teacher.__str__()}"


class StudentCourse(models.Model):
    STATUS_CHOICES = (
        ('P', 'Passed'),
        ('NP', 'Not Passed'),
        ('S', 'Studying'),
        ('NS', 'Not Started'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    semester = models.CharField(max_length=20)
    term = models.PositiveIntegerField()
    avg_mark = models.FloatField(null=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} : {self.course.name}"


def validate_weight(value):
    if value < 1 or value > 100:
        raise ValidationError('Value must be between 1 and 100')


class CoursePartMark(models.Model):
    name = models.CharField(max_length=30)
    weight = models.FloatField(validators=[validate_weight])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} : {self.course.name} : {self.weight}"


def validate_mark(value):
    if value < 0 or value > 10:
        raise ValidationError('Value must be between 0 and 10')


class CourseMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    part_mark = models.ForeignKey(CoursePartMark, on_delete=models.CASCADE)
    mark = models.FloatField(validators=[validate_mark], null=True)

    class Meta:
        unique_together = ('student', 'course', 'part_mark')

    def __str__(self):
        return f"{self.student.name} : {self.course.name} : {self.part_mark.name} : {self.mark}"




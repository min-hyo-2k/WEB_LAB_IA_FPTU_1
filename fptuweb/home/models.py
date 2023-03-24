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
        return f"{self.name} - {self.course_code}"


class CurriculumCourse(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('curriculum', 'course')


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
        return f"{self.name} - {self.roll_number}"


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
        return f"{self.name} - {self.teacher_code}"


class Class(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ClassCourse(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('class_id', 'course')


class ClasCourseStudent(models.Model):
    class_course_id = models.ForeignKey(ClassCourse, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('class_course_id', 'students')


class ClasCourseTeacher(models.Model):
    class_course_id = models.ForeignKey(ClassCourse, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('class_course_id', 'teacher')


class StudentCourse(models.Model):
    STATUS_CHOICES = (
        ('P', 'Passed'),
        ('NP', 'Not Passed'),
        ('S', 'Studying'),
        ('NS', 'Not Started'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    semester = models.CharField(max_length=20)
    term = models.PositiveIntegerField()

    class Meta:
        unique_together = ('student', 'course')


def validate_weight(value):
    if value < 1 or value > 100:
        raise ValidationError('Value must be between 1 and 100')


class CoursePartMark(models.Model):
    name = models.CharField(max_length=30)
    weight = models.FloatField(validators=[validate_weight])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} - {self.course.name}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            total_weight = CoursePartMark.objects.filter(course=self.course).aggregate(total=models.Sum('weight'))['total_weight'] or 0.0
            if total_weight + float(str(self.weight).replace("'", "")) > 100:
                raise ValidationError("The total weight of course parts cannot exceed 100.")
        super().save(*args, **kwargs)


class CourseMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    part_mark = models.ForeignKey(CoursePartMark, on_delete=models.CASCADE)
    mark = models.FloatField()

    class Meta:
        unique_together = ('student', 'course', 'part_mark')

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.part_mark.name} - {self.mark}"

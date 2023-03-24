# Generated by Django 4.1.7 on 2023-03-24 07:27

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('credit', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('major', models.CharField(max_length=10)),
                ('specialization', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-binary')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('date_of_join', models.DateField()),
                ('card_id', models.CharField(max_length=12, unique=True)),
                ('date_of_issue', models.DateField()),
                ('current_term', models.PositiveIntegerField()),
                ('curriculum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-binary')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('date_of_join', models.DateField()),
                ('card_id', models.CharField(max_length=12, unique=True)),
                ('date_of_issue', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CoursePartMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.FloatField(validators=[home.models.validate_weight])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='ClassCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.class')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
            options={
                'unique_together': {('class_id', 'course')},
            },
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Passed'), ('NP', 'Not Passed'), ('S', 'Studying'), ('NS', 'Not Started')], max_length=2)),
                ('semester', models.CharField(max_length=20)),
                ('term', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='CurriculumCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.curriculum')),
            ],
            options={
                'unique_together': {('curriculum', 'course')},
            },
        ),
        migrations.CreateModel(
            name='CourseMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
                ('part_mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.coursepartmark')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
            options={
                'unique_together': {('student', 'course', 'part_mark')},
            },
        ),
        migrations.CreateModel(
            name='ClassCourseTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.classcourse')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.teacher')),
            ],
            options={
                'unique_together': {('class_course_id', 'teacher')},
            },
        ),
        migrations.CreateModel(
            name='ClassCourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.classcourse')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.student')),
            ],
            options={
                'unique_together': {('class_course_id', 'students')},
            },
        ),
    ]
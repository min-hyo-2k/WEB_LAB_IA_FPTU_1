# Generated by Django 4.1.7 on 2023-03-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_studentcourse_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='avg_mark',
            field=models.FloatField(null=True),
        ),
    ]
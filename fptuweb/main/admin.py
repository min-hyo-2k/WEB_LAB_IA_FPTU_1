from django.contrib import admin
from django.apps import apps
from .models import Teacher, Student
# Register your models here.
# admin.site.register(Userlogin)
admin.site.register(Teacher)
admin.site.register(Student)
post_models = apps.get_app_config('main').get_models()

for model in post_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

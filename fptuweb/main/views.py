from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_views(response):
    return render(response, "main/main.html")
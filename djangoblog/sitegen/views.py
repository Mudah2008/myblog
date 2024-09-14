from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "site/home.html")

def resume(request):
    return render(request, "site/resume.html")

def about(request):
    return render(request, "site/about.html")


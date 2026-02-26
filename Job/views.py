from django.shortcuts import render, redirect, get_object_or_404 
from .models import Job 

# Create your views here.

def home(request):
    return render(request, 'Jobs/index.html') 

def add_job(request):
    return render(request, 'Jobs/add_job.html')
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib import messages 
from .models import Job 

# Create your views here.

def home(request):
    
    return render(request, 'Jobs/index.html') 

def add_job(request):
    
    # if request.method == "POST":

    return render(request, 'Jobs/add_job.html')

def all_job(request):
            
    return render(request, 'Jobs/all_job.html')

def browse_job(request):
    
    return render(request, 'Jobs/browse_job.html')

def single_job_view(request):
    
    return render(request, 'Jobs/single_job_view.html')

def edit_job(request):
    
    return render(request, 'Jobs/edit_job.html')

def about_us(request):
    
    return render(request, 'Jobs/about_us.html')
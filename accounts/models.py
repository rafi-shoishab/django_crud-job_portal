from django.db import models
from django.contrib.auth.models import AbstractUser #

# Create your models here.
class CustomUser(AbstractUser): #
    
    ROLE_CHOICES = ( #
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )
    
    display_picture = models.ImageField(upload_to='profile_pic/', null=True, blank=True) #
    role = models.CharField(max_length=30, choices=ROLE_CHOICES) #
    
class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) #
    job_title = models.CharField(max_length=50) 
    company_name = models.CharField(max_length=30) 
    
    def __str__(self):
        return f"recruiter {self.user.username}" #
    
class JobseekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) #
    skill = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return f"Seeker {self.user.username}"
    
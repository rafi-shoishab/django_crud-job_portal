from django.db import models 

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    job_location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    vacancy = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2) 
    deadline = models.DateTimeField(null=True, blank=True) 

    def __str__(self): 
        return self.job_title 
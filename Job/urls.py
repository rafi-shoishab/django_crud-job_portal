from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('add_job/', views.add_job, name='add_job'),
    path('all_job/', views.all_job, name='all_job'),
    path('browse_job/', views.browse_job, name='browse_job'),
]

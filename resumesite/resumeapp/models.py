from typing import Any
from django.db import models
import datetime

# Create your models here.
class Education(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20) 
    
    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Work(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.title
    
class Projects(models.Model):
    title = models.CharField(max_length=200, default="project")
    title_description = models.CharField(max_length=200)
    long_description = models.TextField(max_length=2500)
    gallery_top = models.ImageField()
    gallery_2 = models.ImageField()
    gallery_3 = models.ImageField()
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=200)
    introduction = models.TextField(max_length=4000)
    bio = models.TextField(max_length=20000)
    
    def __str__(self):
        return self.title
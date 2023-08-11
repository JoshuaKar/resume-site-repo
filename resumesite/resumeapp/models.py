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
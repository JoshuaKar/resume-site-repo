from django.shortcuts import render
from django.http import HttpResponse
from .models import Education, Skills, Work

# Create your views here.
def setup(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    education = Education.objects.all()
    skill = Skills.objects.all()
    work = Work.objects.all()
    context = {
        'education': education,
        'skills': skill,
        'work': work,
    }
    print(context)
    return render(request, 'portfolio.html', context)

def projects(request):
    return render(request, 'projects.html')

def links(request):
    return render(request, 'links.html')
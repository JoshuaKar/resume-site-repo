from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Education, Skills, Work, Projects, About

# Create your views here.
def setup(request):
    about = About.objects.all()
    projects = Projects.objects.all()
    context = {
        'about': about,
        'projects': projects,
    }
    return render(request, 'home.html', context)

def health_check(request):
    return HttpResponse("OK", status=200)

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
    #print(context)
    return render(request, 'portfolio.html', context)

def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def single_project(request, title):
    project = get_object_or_404(Projects, title=title)
    return render(request, 'single_project.html', {'project': project})

def links(request):
    return render(request, 'links.html')

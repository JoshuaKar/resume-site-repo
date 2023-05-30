from django.shortcuts import render

# Create your views here.
def setup(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def links(request):
    return render(request, 'links.html')
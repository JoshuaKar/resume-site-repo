from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.setup, name="base"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('projects/', views.projects, name="projects"),
    path('links/', views.links, name="links"),
]
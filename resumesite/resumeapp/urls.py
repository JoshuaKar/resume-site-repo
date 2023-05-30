from django.urls import path
from . import views

urlpatterns = [
    path('', views.setup, name="base"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('links/', views.links, name="links"),
]
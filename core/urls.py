from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search/', views.search_projects, name='search'),
    path('download-resume/', views.download_resume, name='download_resume'),
]
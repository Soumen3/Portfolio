from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('skill/',views.skill, name="skill"),
    path('project/',views.project, name="project"),
    path('contact/',views.contact, name="contact"),
]

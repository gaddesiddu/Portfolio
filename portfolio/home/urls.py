from django.contrib import admin
from django.urls import path, include
from home import views

# Django Admin header customization
admin.site.site_header = "Siddartha"
admin.site.site_title = "Welcome to Siddartha"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("projects", views.projects_view, name="projects"),
    path("resume", views.resume, name="resume"),
]

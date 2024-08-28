from django.shortcuts import render, HttpResponse
from home.models import Contact, Project


# Create your views here.
def home(request):

    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        desc = request.POST["desc"]
        # print(name, email, desc)
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()

    return render(request, "contact.html")


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
def resume(request):
    return render(request, "resume.html")